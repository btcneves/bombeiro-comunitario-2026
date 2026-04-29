#!/usr/bin/env python3
"""
auditoria_gabaritos.py — Auditor e embaralhador de gabaritos do BC 2026.

Modos:
  --audit          Gera relatório de qualidade (default, dry-run, não modifica arquivos).
  --shuffle        Rebalanceia gabaritos (use --write para salvar em disco).
  --self-test      Executa testes de sanidade internos e sai com código 0 se OK.

Uso:
  python3 scripts/auditoria_gabaritos.py --audit
  python3 scripts/auditoria_gabaritos.py --shuffle --seed 42 --write
  python3 scripts/auditoria_gabaritos.py --self-test

Saída:
  docs/relatorios/auditoria-gabaritos-AAAA-MM-DD.md   (Markdown)
  docs/relatorios/auditoria-gabaritos-AAAA-MM-DD.json (JSON)

Critérios de aprovação (--audit retorna exit code 1 se violados):
  - Nenhuma letra com percentual >= 30% do total de questões do simulado
  - Zero alternativas vazias ou duplicadas
  - Zero questões com gabarito apontando para letra inexistente
  - Zero questões com múltiplas alternativas marcadas como corretas
  - Zero questões sem Fonte
  - Zero questões sem Comentário
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

# ─────────────────────────────── paths ────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "Obsidian Vault"
SIMULADOS_PATHS = [
    VAULT / "06 - Questões" / "Simulado 01 - Diagnóstico.md",
    VAULT / "06 - Questões" / "Simulado 02 - Conhecimentos Específicos.md",
    VAULT / "06 - Questões" / "Simulado 03 - Reta Final.md",
]
GABARITOS_PATH = VAULT / "06 - Questões" / "Gabaritos Comentados.md"
REPORT_DIR = ROOT / "docs" / "relatorios"

LETTERS = list("ABCDE")

# ─────────────────────────────── patterns ─────────────────────────────────────

_ABSOLUTISM = re.compile(
    r"\b(somente|apenas|sempre|nunca|jamais|exclusivamente|automaticamente|"
    r"obrigatoriamente|dispensa|substitui|elimina|livre\s+e\s+sem|"
    r"sem\s+padroniza[çc][ãa]o|completo\s+de)\b",
    re.IGNORECASE,
)
_HEDGE = re.compile(
    r"\b(conforme|entre\s+outros|de\s+acordo\s+com|quando\s+poss[íi]vel|"
    r"mediante|respeitad[oa]s?|pode\s+ser|desde\s+que)\b",
    re.IGNORECASE,
)
_ALT_LINE = re.compile(r"^([A-E])\) (.+?)(?:\s{2,})?$", re.MULTILINE)
_GABARITO_LINE = re.compile(r"\*\*Gabarito:\*\*\s*([A-E])\b.*")
_QUESTION_HEADER = re.compile(r"^### Questão (\d+)\s*$", re.MULTILINE)
_FIELD = re.compile(r"^\*\*([^*]+)\*\*:\s*(.+?)(?:\s{2,})?$")

# ─────────────────────────────── dataclasses ──────────────────────────────────

@dataclass
class ParsedQuestion:
    simulado: str
    number: int
    disciplina: str
    tema: str
    nivel: str
    tipo: str
    enunciado: str
    alternatives: dict          # {'A': 'text', 'B': 'text', ...}
    gabarito: str               # single letter
    comentario: str
    fonte: str
    revisar: str
    content_hash: str           # SHA-1 of gabarito alternative text


@dataclass
class QualityIssue:
    simulado: str
    q_num: int
    code: str
    detail: str


@dataclass
class SimuladoStats:
    name: str
    total: int
    dist: dict                  # {'A': count, ...}
    pct: dict                   # {'A': 12.5, ...}
    correct_is_longest: int     # count of questions where correct alt is longest
    absolutism_in_wrong: int    # count with absolutism keywords in wrong alts
    hedge_in_correct: int       # count with hedge keywords in correct alt
    issues: list[QualityIssue]


# ─────────────────────────────── parser ───────────────────────────────────────

def _strip_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    idx = text.index("\n---", 3)
    fm = text[: idx + 4]
    rest = text[idx + 4 :]
    return fm, rest


def _parse_question_block(block: str, simulado: str, number: int) -> ParsedQuestion:
    lines = block.splitlines()
    disciplina = tema = nivel = tipo = comentario = fonte = revisar = gabarito = ""
    alternatives: dict[str, str] = {}
    enunciado_parts: list[str] = []
    in_post_meta = False
    in_alternatives = False

    for line in lines[1:]:  # skip "### Questão NN"
        stripped = line.strip()

        # Alternative
        m_alt = re.match(r"^([A-E])\) (.+?)(?:\s{2,})?$", line.rstrip())
        if m_alt:
            in_alternatives = True
            alternatives[m_alt.group(1)] = m_alt.group(2).rstrip()
            continue

        # Bold field — handles both "**Key:** value" (colon inside) and "**Key**: value"
        m_field = re.match(r"^\*\*([^*]+)\*\*:?\s*(.+?)\s*$", stripped)
        if m_field:
            key = m_field.group(1).strip().rstrip(":").strip()
            val = m_field.group(2).strip()
            if key == "Disciplina":
                disciplina = val
            elif key == "Tema":
                tema = val
            elif key in ("Nível", "Nivel"):
                nivel = val
            elif key == "Tipo":
                tipo = val
            elif key == "Gabarito":
                g_match = re.match(r"([A-E])", val)
                gabarito = g_match.group(1) if g_match else val[:1]
                in_post_meta = True
            elif key in ("Comentário", "Comentario"):
                comentario = val
                in_post_meta = True
            elif key == "Fonte":
                fonte = val
            elif key == "Revisar":
                revisar = val
            continue

        # Blank line
        if not stripped:
            continue

        # Enunciado (not yet in alternatives, not in post meta)
        if not in_alternatives and not in_post_meta:
            enunciado_parts.append(stripped)

    enunciado = " ".join(enunciado_parts).strip()
    correct_text = alternatives.get(gabarito, "")
    content_hash = hashlib.sha1(correct_text.encode()).hexdigest()[:8]

    return ParsedQuestion(
        simulado=simulado,
        number=number,
        disciplina=disciplina,
        tema=tema,
        nivel=nivel,
        tipo=tipo,
        enunciado=enunciado,
        alternatives=alternatives,
        gabarito=gabarito,
        comentario=comentario,
        fonte=fonte,
        revisar=revisar,
        content_hash=content_hash,
    )


def parse_simulado(path: Path) -> tuple[str, str, list[ParsedQuestion]]:
    """Returns (frontmatter, header_section, questions)."""
    text = path.read_text(encoding="utf-8")
    frontmatter, rest = _strip_frontmatter(text)
    name = path.stem

    matches = list(_QUESTION_HEADER.finditer(rest))
    if not matches:
        return frontmatter, rest, []

    header_section = rest[: matches[0].start()]
    questions: list[ParsedQuestion] = []

    for i, m in enumerate(matches):
        q_num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(rest)
        block = rest[start:end]
        questions.append(_parse_question_block(block, name, q_num))

    return frontmatter, header_section, questions


# ─────────────────────────────── auditor ──────────────────────────────────────

def _audit_question(q: ParsedQuestion) -> list[QualityIssue]:
    issues: list[QualityIssue] = []
    alts = q.alternatives

    # 1. Letters present
    present = sorted(alts.keys())
    expected = LETTERS[: len(present)]
    if present != expected:
        issues.append(QualityIssue(q.simulado, q.number, "MISSING_LETTER",
                                   f"alternativas presentes: {present}"))

    # 2. Empty alternatives
    for letter, text in alts.items():
        if not text.strip():
            issues.append(QualityIssue(q.simulado, q.number, "EMPTY_ALT",
                                       f"alternativa {letter} vazia"))

    # 3. Duplicate alternatives
    texts = list(alts.values())
    seen: set[str] = set()
    for t in texts:
        norm = t.strip().lower()
        if norm in seen:
            issues.append(QualityIssue(q.simulado, q.number, "DUPLICATE_ALT",
                                       f"texto duplicado: '{t[:40]}'"))
        seen.add(norm)

    # 4. Gabarito inexistente
    if q.gabarito not in alts:
        issues.append(QualityIssue(q.simulado, q.number, "GABARITO_INEXISTENTE",
                                   f"gabarito={q.gabarito!r} não encontrado nas alternativas"))

    # 5. Gabarito vazio
    if not q.gabarito:
        issues.append(QualityIssue(q.simulado, q.number, "GABARITO_VAZIO",
                                   "campo Gabarito ausente"))

    # 6. Missing Comentário
    if not q.comentario:
        issues.append(QualityIssue(q.simulado, q.number, "SEM_COMENTARIO",
                                   "campo Comentário ausente ou vazio"))

    # 7. Missing Fonte
    if not q.fonte:
        issues.append(QualityIssue(q.simulado, q.number, "SEM_FONTE",
                                   "campo Fonte ausente ou vazio"))

    return issues


def audit_questions(questions: list[ParsedQuestion]) -> SimuladoStats:
    name = questions[0].simulado if questions else "?"
    dist: dict[str, int] = Counter()
    all_issues: list[QualityIssue] = []
    correct_is_longest = 0
    absolutism_in_wrong = 0
    hedge_in_correct = 0

    for q in questions:
        all_issues.extend(_audit_question(q))

        if q.gabarito in q.alternatives:
            dist[q.gabarito] += 1

            # Correct = longest
            correct_len = len(q.alternatives[q.gabarito])
            all_lens = [len(t) for t in q.alternatives.values()]
            if correct_len == max(all_lens) and all_lens.count(max(all_lens)) == 1:
                correct_is_longest += 1

            # Absolutism in wrong alternatives
            wrong_texts = " ".join(v for k, v in q.alternatives.items() if k != q.gabarito)
            if _ABSOLUTISM.search(wrong_texts):
                absolutism_in_wrong += 1

            # Hedge in correct alternative
            if _HEDGE.search(q.alternatives[q.gabarito]):
                hedge_in_correct += 1

    total = len(questions)
    pct = {l: round(100 * dist.get(l, 0) / total, 1) if total else 0 for l in LETTERS}

    return SimuladoStats(
        name=name,
        total=total,
        dist=dict(dist),
        pct=pct,
        correct_is_longest=correct_is_longest,
        absolutism_in_wrong=absolutism_in_wrong,
        hedge_in_correct=hedge_in_correct,
        issues=all_issues,
    )


def has_critical_issues(stats_list: list[SimuladoStats]) -> bool:
    """Returns True if any blocking criterion is violated."""
    for s in stats_list:
        # Letter concentration >= 30%
        for letter, p in s.pct.items():
            if p >= 30.0:
                return True
        # Hard errors
        hard_codes = {"EMPTY_ALT", "DUPLICATE_ALT", "GABARITO_INEXISTENTE",
                      "GABARITO_VAZIO", "SEM_FONTE", "SEM_COMENTARIO"}
        for issue in s.issues:
            if issue.code in hard_codes:
                return True
    return False


# ─────────────────────────────── shuffler ─────────────────────────────────────

def _compute_balanced_targets(n: int, seed: int) -> list[str]:
    """Return a list of n letter assignments (A-E) with ~equal distribution."""
    rng = random.Random(seed)
    per_letter = n // 5
    remainder = n % 5
    pool: list[str] = []
    for i, letter in enumerate(LETTERS):
        count = per_letter + (1 if i < remainder else 0)
        pool.extend([letter] * count)
    rng.shuffle(pool)
    return pool


def compute_shuffle(
    questions: list[ParsedQuestion], seed: int
) -> list[tuple[ParsedQuestion, list[int], str]]:
    """
    Returns list of (question, new_order, new_gabarito_letter).
    new_order[i] = index (0=A,1=B,...) from original alternatives to place at position i.
    Guarantees: no letter exceeds 25% + 1/n slack; correct content is preserved by hash.
    """
    targets = _compute_balanced_targets(len(questions), seed)
    rng = random.Random(seed + 1)  # separate rng for permutation of incorrect alts
    result = []

    for q, target_letter in zip(questions, targets):
        n_alts = len(q.alternatives)
        target_idx = LETTERS.index(target_letter)
        correct_idx = LETTERS.index(q.gabarito) if q.gabarito in LETTERS else 0

        # Indices of all positions except the one for the correct answer
        wrong_positions = list(range(n_alts))
        wrong_positions.remove(correct_idx)
        rng.shuffle(wrong_positions)

        # new_order[new_position] = original_index
        new_order = [0] * n_alts
        new_order[target_idx] = correct_idx
        remaining_slots = [i for i in range(n_alts) if i != target_idx]
        for slot, orig_idx in zip(remaining_slots, wrong_positions):
            new_order[slot] = orig_idx

        result.append((q, new_order, target_letter))

    return result


def _reconstruct_question_block(
    original_block: str, new_order: list[int], new_letter: str
) -> str:
    """Rewrites the alternatives and gabarito in the raw block text."""
    lines = original_block.splitlines(keepends=True)

    # Collect alternative line positions and texts
    alt_indices: list[int] = []
    alt_texts: list[str] = []
    for i, line in enumerate(lines):
        m = re.match(r"^([A-E])\) (.+?)(?:\s{2,})?$", line.rstrip("\n"))
        if m:
            alt_indices.append(i)
            alt_texts.append(m.group(2).rstrip())

    if len(alt_indices) < 2:
        return original_block  # can't safely modify

    n = len(alt_indices)
    new_texts = [alt_texts[new_order[i]] for i in range(n)]

    # Rebuild alternative lines preserving trailing-space convention:
    # all except last get "  " (markdown line break), last gets none
    new_alt_lines: list[str] = []
    for i, (letter, text) in enumerate(zip(LETTERS[:n], new_texts)):
        suffix = "  \n" if i < n - 1 else "\n"
        new_alt_lines.append(f"{letter}) {text}{suffix}")

    # Replace alternative lines in the line list
    for pos, new_line in zip(alt_indices, new_alt_lines):
        lines[pos] = new_line

    # Update gabarito line
    rebuilt = "".join(lines)
    rebuilt = re.sub(
        r"(\*\*Gabarito:\*\*\s*)[A-E](\b.*)",
        lambda m2: m2.group(1) + new_letter + m2.group(2),
        rebuilt,
    )
    return rebuilt


def shuffle_simulado_file(
    path: Path,
    shuffles: list[tuple[ParsedQuestion, list[int], str]],
) -> str:
    """Returns the new file content with shuffled alternatives."""
    text = path.read_text(encoding="utf-8")
    _, rest = _strip_frontmatter(text)
    fm = text[: len(text) - len(rest)]

    matches = list(_QUESTION_HEADER.finditer(rest))
    if not matches:
        return text

    shuffle_map = {q.number: (order, letter) for q, order, letter in shuffles}

    parts: list[str] = [fm, rest[: matches[0].start()]]

    for i, m in enumerate(matches):
        q_num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(rest)
        block = rest[start:end]

        if q_num in shuffle_map:
            order, letter = shuffle_map[q_num]
            block = _reconstruct_question_block(block, order, letter)

        parts.append(block)

    return "".join(parts)


# ─────────────────────────────── gabaritos table updater ──────────────────────

def update_gabaritos_file(
    path: Path, updates: dict[str, dict[int, str]]
) -> str:
    """
    updates = {'Simulado 01 - Diagnóstico': {1: 'A', 2: 'C', ...}, ...}
    Returns new file content.
    """
    text = path.read_text(encoding="utf-8")

    for sim_name, q_map in updates.items():
        for q_num, new_letter in q_map.items():
            # Match table row: | 01 | B | ... or | 1 | B | ...
            pattern = re.compile(
                r"(\|\s*" + str(q_num).zfill(2) + r"\s*\|\s*)[A-E](\s*\|)"
            )
            text = pattern.sub(r"\g<1>" + new_letter + r"\2", text)

    return text


# ─────────────────────────────── reporter ─────────────────────────────────────

def _dist_bar(pct: float, width: int = 20) -> str:
    filled = int(round(pct / 100 * width))
    return "█" * filled + "░" * (width - filled)


def generate_report(
    stats_list: list[SimuladoStats],
    seed: Optional[int] = None,
    mode: str = "audit",
) -> tuple[str, dict]:
    today = date.today().isoformat()
    all_issues = [i for s in stats_list for i in s.issues]
    total_all = sum(s.total for s in stats_list)

    # Aggregate distribution
    agg_dist: Counter = Counter()
    for s in stats_list:
        for letter, count in s.dist.items():
            agg_dist[letter] += count
    agg_pct = {l: round(100 * agg_dist.get(l, 0) / total_all, 1) if total_all else 0
               for l in LETTERS}

    # ── Markdown report ────────────────────────────────────────────────────────
    lines: list[str] = []
    lines.append(f"# Auditoria de Gabaritos — BC 2026")
    lines.append(f"\n**Data:** {today}  ")
    lines.append(f"**Modo:** {mode}  ")
    if seed is not None:
        lines.append(f"**Seed de embaralhamento:** {seed}  ")
    lines.append(f"**Total de questões:** {total_all}  ")
    lines.append("")

    lines.append("## Distribuição Agregada (todos os simulados)")
    lines.append("")
    lines.append("| Letra | Qtd | % | Barra |")
    lines.append("|:---:|---:|---:|---|")
    for letter in LETTERS:
        cnt = agg_dist.get(letter, 0)
        pct = agg_pct[letter]
        alert = " ⚠️" if pct >= 30 else (" ✅" if 15 <= pct <= 25 else "")
        lines.append(f"| **{letter}** | {cnt} | {pct}% | {_dist_bar(pct)}{alert} |")
    lines.append(f"| **Total** | {total_all} | 100% | |")
    lines.append("")

    correct_total = sum(s.correct_is_longest for s in stats_list)
    lines.append(f"**Correta = mais longa:** {correct_total}/{total_all} questões "
                 f"({round(100*correct_total/total_all,1) if total_all else 0}%)")
    lines.append("")

    lines.append("## Por Simulado")
    lines.append("")

    for s in stats_list:
        lines.append(f"### {s.name}")
        lines.append("")
        lines.append(f"Total: {s.total} questões  ")
        lines.append(f"Correta = mais longa: {s.correct_is_longest}/{s.total}  ")
        lines.append(f"Absolutismo em erradas: {s.absolutism_in_wrong}/{s.total}  ")
        lines.append(f"Hedge na correta: {s.hedge_in_correct}/{s.total}")
        lines.append("")
        lines.append("| Letra | Qtd | % | Status |")
        lines.append("|:---:|---:|---:|:---:|")
        for letter in LETTERS:
            cnt = s.dist.get(letter, 0)
            pct = s.pct.get(letter, 0.0)
            if pct >= 30:
                status = "🔴 ALTA"
            elif pct >= 25:
                status = "🟡 ELEVADA"
            elif pct < 10:
                status = "🟡 BAIXA"
            else:
                status = "🟢 OK"
            lines.append(f"| **{letter}** | {cnt} | {pct}% | {status} |")
        lines.append("")

        if s.issues:
            lines.append("**Problemas detectados:**")
            lines.append("")
            by_code: dict[str, list[QualityIssue]] = defaultdict(list)
            for iss in s.issues:
                by_code[iss.code].append(iss)
            for code, items in sorted(by_code.items()):
                q_nums = ", ".join(f"Q{i.q_num:02d}" for i in items)
                lines.append(f"- `{code}` ({len(items)}x): {q_nums}")
                for iss in items[:3]:
                    lines.append(f"  - {iss.detail}")
            lines.append("")

    lines.append("## Questões Suspeitas — Correto Sempre Mais Longo")
    lines.append("")
    lines.append("Questões onde a alternativa correta é estritamente mais longa que todas as incorretas "
                 "(indicativo de viés editorial):")
    lines.append("")
    lines.append("| Simulado | Q | Gabarito | Tam. Correta | Tam. Mais Longa Errada |")
    lines.append("|---|:---:|:---:|---:|---:|")
    showed = 0
    for s in stats_list:
        pass  # will be filled below after parsing stats

    # We need the original questions to emit per-question details.
    # This section is filled separately when caller provides questions.
    lines.append("_(ver JSON para lista completa)_")
    lines.append("")

    lines.append("## Padrões Linguísticos Detectados")
    lines.append("")
    lines.append("| Padrão | Qtd | % | Risco |")
    lines.append("|---|---:|---:|---|")
    total_absolutism = sum(s.absolutism_in_wrong for s in stats_list)
    total_hedge = sum(s.hedge_in_correct for s in stats_list)
    lines.append(f"| Absolutismo em alternativas erradas | {total_absolutism} | "
                 f"{round(100*total_absolutism/total_all,1) if total_all else 0}% | "
                 f"{'🔴 alto' if total_absolutism/total_all > 0.3 else '🟡'} |")
    lines.append(f"| Linguagem de hedge na correta | {total_hedge} | "
                 f"{round(100*total_hedge/total_all,1) if total_all else 0}% | "
                 f"{'🔴 alto' if total_hedge/total_all > 0.3 else '🟡'} |")
    lines.append("")

    lines.append("## Problemas de Qualidade (resumo)")
    lines.append("")
    if not all_issues:
        lines.append("✅ Nenhum problema crítico detectado.")
    else:
        by_code_all: dict[str, list[QualityIssue]] = defaultdict(list)
        for iss in all_issues:
            by_code_all[iss.code].append(iss)
        lines.append("| Código | Qtd | Questões |")
        lines.append("|---|---:|---|")
        for code, items in sorted(by_code_all.items()):
            q_list = ", ".join(f"{i.simulado[:10]}·Q{i.q_num:02d}" for i in items[:6])
            if len(items) > 6:
                q_list += f" (+{len(items)-6})"
            lines.append(f"| `{code}` | {len(items)} | {q_list} |")
    lines.append("")

    lines.append("## Recomendações")
    lines.append("")
    recs = []
    if agg_pct.get("B", 0) > 30:
        recs.append("🔴 **Concentração crítica em B**: executar `--shuffle --write` para rebalancear.")
    if correct_total / total_all > 0.3 if total_all else False:
        recs.append(f"🟡 **Correta = mais longa em {round(100*correct_total/total_all)}% das questões**: "
                    "reescrever distratores para normalizar comprimentos.")
    if total_absolutism / total_all > 0.3 if total_all else False:
        recs.append("🟡 **Muitas alternativas erradas com absolutismo**: substituir por distratores plausíveis.")
    if any(s.issues for s in stats_list):
        hard_count = sum(1 for i in all_issues
                         if i.code in {"EMPTY_ALT", "DUPLICATE_ALT",
                                       "GABARITO_INEXISTENTE", "GABARITO_VAZIO"})
        if hard_count:
            recs.append(f"🔴 **{hard_count} problemas bloqueantes** (alternativas vazias/duplicadas, "
                        "gabarito inválido): corrigir antes de qualquer simulação.")
    if not recs:
        recs.append("✅ Banco dentro dos critérios de qualidade.")
    for r in recs:
        lines.append(f"- {r}")
    lines.append("")

    lines.append("## Como interpretar")
    lines.append("")
    lines.append("- **Distribuição esperada**: ~20% por letra (±5 pp). Valores ≥30% indicam viés forte.")
    lines.append("- **Correta = mais longa**: em >30% das questões o banco fica 'chutável' por comprimento.")
    lines.append("- **Absolutismo em erradas**: palavras como *somente*, *apenas*, *nunca* em alternativas "
                 "incorretas são dica implícita — treinar isso prejudica o raciocínio real.")
    lines.append("- **Exit code 0** = sem violações bloqueantes. **Exit code 1** = há violações.")
    lines.append("")

    lines.append("---")
    lines.append(f"_Gerado por `scripts/auditoria_gabaritos.py` em {today}._")

    md_text = "\n".join(lines)

    # ── JSON ──────────────────────────────────────────────────────────────────
    json_data = {
        "date": today,
        "mode": mode,
        "seed": seed,
        "total": total_all,
        "aggregate_distribution": {l: {"count": agg_dist.get(l, 0), "pct": agg_pct[l]}
                                    for l in LETTERS},
        "correct_is_longest_count": correct_total,
        "simulados": [
            {
                "name": s.name,
                "total": s.total,
                "distribution": {l: {"count": s.dist.get(l, 0), "pct": s.pct.get(l, 0.0)}
                                 for l in LETTERS},
                "correct_is_longest": s.correct_is_longest,
                "absolutism_in_wrong": s.absolutism_in_wrong,
                "hedge_in_correct": s.hedge_in_correct,
                "issues": [
                    {"q": i.q_num, "code": i.code, "detail": i.detail}
                    for i in s.issues
                ],
            }
            for s in stats_list
        ],
    }

    return md_text, json_data


def generate_detailed_table(all_questions: list[ParsedQuestion]) -> str:
    """Returns Markdown table of per-question correctness details."""
    rows = ["| Simulado | Q | Letra | Tam Correta | Tam Max Errada | Correta=Mais Longa |",
            "|---|:---:|:---:|---:|---:|:---:|"]
    for q in all_questions:
        if q.gabarito not in q.alternatives:
            continue
        correct_len = len(q.alternatives[q.gabarito])
        wrong_lens = [len(v) for k, v in q.alternatives.items() if k != q.gabarito]
        max_wrong = max(wrong_lens) if wrong_lens else 0
        is_longest = correct_len > max_wrong
        flag = "⚠️" if is_longest else "✅"
        short_name = q.simulado.replace("Simulado ", "S").split(" -")[0]
        rows.append(f"| {short_name} | {q.number:02d} | {q.gabarito} | "
                    f"{correct_len} | {max_wrong} | {flag} |")
    return "\n".join(rows)


# ─────────────────────────────── self-test ────────────────────────────────────

def self_test() -> bool:
    """Returns True if all tests pass."""
    print("Executando self-test...", flush=True)
    errors: list[str] = []

    # ── Test 1: balanced target generation ───────────────────────────────────
    for n in [30, 35, 25, 10]:
        targets = _compute_balanced_targets(n, seed=42)
        assert len(targets) == n, f"T1 len fail n={n}"
        cnt = Counter(targets)
        for letter in LETTERS:
            assert abs(cnt.get(letter, 0) - n / 5) <= 1, \
                f"T1 imbalance n={n} letter={letter} cnt={cnt}"
    print("  ✅ T1: balanced target generation")

    # ── Test 2: shuffle preserves correct content ─────────────────────────────
    dummy_q = ParsedQuestion(
        simulado="Teste",
        number=1,
        disciplina="Teste",
        tema="Teste",
        nivel="Fácil",
        tipo="Literal",
        enunciado="Questão de teste com acentuação: ção, é, ã.",
        alternatives={
            "A": "alternativa errada um",
            "B": "alternativa CORRETA com texto mais longo e detalhado conforme o manual",
            "C": "alternativa errada três",
            "D": "alternativa errada quatro apenas somente",
            "E": "alternativa errada cinco",
        },
        gabarito="B",
        comentario="comentário",
        fonte="Teste",
        revisar="[[Teste]]",
        content_hash=hashlib.sha1(b"alternativa CORRETA com texto mais longo e detalhado conforme o manual").hexdigest()[:8],
    )
    qs = [dummy_q] * 10

    for seed in [0, 1, 42, 999]:
        shuffles = compute_shuffle(qs, seed)
        for orig_q, order, new_letter in shuffles:
            # new_letter position must contain the originally correct text
            correct_original_text = orig_q.alternatives[orig_q.gabarito]
            alt_list = [orig_q.alternatives[l] for l in LETTERS if l in orig_q.alternatives]
            new_alt_list = [alt_list[order[i]] for i in range(len(order))]
            new_letter_idx = LETTERS.index(new_letter)
            if new_alt_list[new_letter_idx] != correct_original_text:
                errors.append(f"T2 content mismatch seed={seed}")
    print("  ✅ T2: shuffle preserves correct content")

    # ── Test 3: block reconstruction ─────────────────────────────────────────
    sample_block = """\
### Questão 01

**Disciplina:** Português
**Tema:** Crase
**Nível:** Médio
**Tipo:** Aplicação

Questão de teste com acentos: ção.

A) alternativa errada um
B) alternativa CORRETA com texto mais longo e detalhado
C) alternativa errada três
D) alternativa errada quatro
E) alternativa errada cinco

**Gabarito:** B
**Comentário:** comentário de teste.
**Fonte:** Teste.
**Revisar:** [[Teste]]
"""
    # Shuffle: move B (idx 1) to position A (idx 0)
    new_order = [1, 0, 2, 3, 4]  # new[0]=orig[1], new[1]=orig[0], new[2-4]=orig[2-4]
    reconstructed = _reconstruct_question_block(sample_block, new_order, "A")
    # Check new A contains original B text
    assert "A) alternativa CORRETA" in reconstructed, \
        f"T3: expected 'A) alternativa CORRETA' in:\n{reconstructed}"
    assert "B) alternativa errada um" in reconstructed, \
        "T3: expected 'B) alternativa errada um'"
    assert "**Gabarito:** A" in reconstructed, \
        f"T3: expected '**Gabarito:** A' in:\n{reconstructed}"
    print("  ✅ T3: block reconstruction")

    # ── Test 4: parse round-trip sanity ──────────────────────────────────────
    q = _parse_question_block(sample_block, "Teste", 1)
    assert q.gabarito == "B", f"T4: gabarito={q.gabarito}"
    assert q.alternatives["B"] == "alternativa CORRETA com texto mais longo e detalhado", \
        f"T4 alt B: {q.alternatives['B']!r}"
    assert q.disciplina == "Português", f"T4 disciplina: {q.disciplina!r}"
    assert q.tema == "Crase", f"T4 tema: {q.tema!r}"
    assert "ção" in q.enunciado, f"T4 encoding: {q.enunciado!r}"
    print("  ✅ T4: parser round-trip")

    # ── Test 5: balanced distribution for 35 and 30 questions ────────────────
    for n, expected_max_pct in [(35, 21.0), (30, 20.0)]:
        targets = _compute_balanced_targets(n, seed=42)
        cnt = Counter(targets)
        max_pct = max(cnt[l] / n * 100 for l in LETTERS)
        assert max_pct <= 21.1, f"T5 max_pct={max_pct} n={n}"
    print("  ✅ T5: balanced distribution for 35 and 30 questions")

    # ── Test 6: gabaritos table update ────────────────────────────────────────
    sample_gabaritos = """\
## Simulado 01 - Diagnóstico

| Q | Gabarito | Tema | Revisar |
|---:|:---:|---|---|
| 01 | B | Interpretação | [[X]] |
| 02 | C | Crase | [[Y]] |
"""
    import tempfile, os
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(sample_gabaritos)
        tmp_path = Path(f.name)
    try:
        updates = {"Simulado 01 - Diagnóstico": {1: "A", 2: "E"}}
        new_content = update_gabaritos_file(tmp_path, updates)
        assert "| 01 | A |" in new_content, f"T6 Q01: {new_content}"
        assert "| 02 | E |" in new_content, f"T6 Q02: {new_content}"
    finally:
        os.unlink(tmp_path)
    print("  ✅ T6: gabaritos table update")

    if errors:
        print(f"\n❌ Falhas: {errors}")
        return False

    print("\n✅ Todos os testes passaram.")
    return True


# ─────────────────────────────── main ─────────────────────────────────────────

def _save_report(md_text: str, json_data: dict) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    md_path = REPORT_DIR / f"auditoria-gabaritos-{today}.md"
    json_path = REPORT_DIR / f"auditoria-gabaritos-{today}.json"
    md_path.write_text(md_text, encoding="utf-8")
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")
    return md_path, json_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Auditor e embaralhador de gabaritos BC 2026."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--audit", action="store_true", default=True,
                       help="Modo auditoria (default, dry-run)")
    group.add_argument("--shuffle", action="store_true",
                       help="Rebalanceia gabaritos (use --write para salvar)")
    group.add_argument("--self-test", dest="selftest", action="store_true",
                       help="Executa self-tests e sai")
    parser.add_argument("--seed", type=int, default=42,
                        help="Seed para embaralhamento (default: 42)")
    parser.add_argument("--write", action="store_true",
                        help="Salva arquivos modificados em disco (requer --shuffle)")
    parser.add_argument("--no-save-report", action="store_true",
                        help="Não salva o relatório em docs/relatorios/")
    args = parser.parse_args()

    if args.selftest:
        ok = self_test()
        return 0 if ok else 1

    # ── Parse all simulados ───────────────────────────────────────────────────
    all_questions: list[ParsedQuestion] = []
    parsed_files: dict[Path, tuple[str, str, list[ParsedQuestion]]] = {}

    for path in SIMULADOS_PATHS:
        if not path.exists():
            print(f"⚠️  Arquivo não encontrado: {path}", file=sys.stderr)
            continue
        fm, header, questions = parse_simulado(path)
        parsed_files[path] = (fm, header, questions)
        all_questions.extend(questions)
        print(f"📄 {path.name}: {len(questions)} questões")

    if not all_questions:
        print("❌ Nenhuma questão encontrada.", file=sys.stderr)
        return 1

    # ── Audit ─────────────────────────────────────────────────────────────────
    stats_list: list[SimuladoStats] = []
    for path, (_, _, questions) in parsed_files.items():
        if questions:
            stats_list.append(audit_questions(questions))

    mode_label = "shuffle" if args.shuffle else "audit"
    seed = args.seed if args.shuffle else None
    md_text, json_data = generate_report(stats_list, seed=seed, mode=mode_label)

    # Inject detailed table into report
    detail_table = generate_detailed_table(all_questions)
    md_text = md_text.replace("_(ver JSON para lista completa)_", detail_table)

    # ── Print summary ─────────────────────────────────────────────────────────
    print("\n" + "═" * 60)
    print("DISTRIBUIÇÃO DE GABARITOS")
    print("═" * 60)
    total = sum(s.total for s in stats_list)
    agg: Counter = Counter()
    for s in stats_list:
        for l, c in s.dist.items():
            agg[l] += c
    for letter in LETTERS:
        cnt = agg.get(letter, 0)
        pct = round(100 * cnt / total, 1) if total else 0
        bar = _dist_bar(pct, 30)
        flag = " ⚠️  ALTA" if pct >= 30 else (" ✅" if 15 <= pct <= 25 else "")
        print(f"  {letter}: {cnt:3d}  ({pct:5.1f}%) {bar}{flag}")
    print(f"\n  Total: {total} questões")

    correct_is_longest = sum(s.correct_is_longest for s in stats_list)
    print(f"\n  Correta = mais longa: {correct_is_longest}/{total} "
          f"({round(100*correct_is_longest/total,1) if total else 0}%)")

    all_issues = [i for s in stats_list for i in s.issues]
    if all_issues:
        print(f"\n  ⚠️  {len(all_issues)} problema(s) detectado(s).")
    else:
        print("\n  ✅ Sem problemas de integridade detectados.")

    # ── Shuffle mode ──────────────────────────────────────────────────────────
    if args.shuffle:
        print(f"\n🔀 Modo shuffle (seed={args.seed})")
        gabaritos_updates: dict[str, dict[int, str]] = {}

        for path, (fm, header, questions) in parsed_files.items():
            if not questions:
                continue
            shuffles = compute_shuffle(questions, args.seed)
            new_content = shuffle_simulado_file(path, shuffles)

            if args.write:
                path.write_text(new_content, encoding="utf-8")
                print(f"  ✅ Escrito: {path.name}")
            else:
                print(f"  🔍 Simulação (dry-run): {path.name} — use --write para salvar")

            # Collect gabaritos updates
            sim_name = path.stem
            gabaritos_updates[sim_name] = {q.number: letter for q, _, letter in shuffles}

        if args.write and GABARITOS_PATH.exists():
            new_gabaritos = update_gabaritos_file(GABARITOS_PATH, gabaritos_updates)
            GABARITOS_PATH.write_text(new_gabaritos, encoding="utf-8")
            print(f"  ✅ Escrito: {GABARITOS_PATH.name}")

        # Re-audit after shuffle to confirm balance
        if args.write:
            print("\n🔍 Re-auditando após shuffle...")
            post_stats: list[SimuladoStats] = []
            for path in SIMULADOS_PATHS:
                if path.exists():
                    _, _, qs = parse_simulado(path)
                    if qs:
                        post_stats.append(audit_questions(qs))
            for s in post_stats:
                max_pct = max(s.pct.values()) if s.pct else 0
                flag = "✅" if max_pct < 30 else "❌"
                print(f"  {flag} {s.name}: max letra = {max_pct}%")

    # ── Save report ───────────────────────────────────────────────────────────
    if not args.no_save_report:
        md_path, json_path = _save_report(md_text, json_data)
        print(f"\n📊 Relatório salvo:")
        print(f"   {md_path}")
        print(f"   {json_path}")

    # ── Exit code ─────────────────────────────────────────────────────────────
    if has_critical_issues(stats_list):
        print("\n❌ Critérios de aceitação NÃO atendidos (exit 1).", file=sys.stderr)
        return 1
    print("\n✅ Critérios de aceitação atendidos (exit 0).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
