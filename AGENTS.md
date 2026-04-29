# AGENTS.md — Contrato de Agente para BC 2026

> Leia este arquivo antes de qualquer interação com o repositório. Aplica-se a Claude, Codex, ChatGPT, Cursor, Aider e qualquer outro agente assistido por IA.

## Visão em 60 segundos

Repositório de estudo pessoal para o concurso **Bombeiro Comunitário SC 2026 (BC 2026)**. Estrutura:

- `Obsidian Vault/` — segundo cérebro em Markdown (notas atômicas, simulados, flashcards, revisões)
- `scripts/` — ferramentas de auditoria e manutenção (Python 3 stdlib)
- `docs/` — documentação técnica, relatórios e ADRs
- Sem backend, sem framework, sem dependências externas além de Obsidian

## Regras Obrigatórias

### 🔴 Gabaritos e Qualidade das Questões

1. **Nunca criar ou editar questões com gabarito concentrado em B** (ou em qualquer letra). A distribuição alvo é 20% ±5% por letra (A/B/C/D/E).
2. **Sempre rodar a auditoria antes de fazer commit com questões novas ou modificadas:**
   ```bash
   python3 scripts/auditoria_gabaritos.py --audit
   # Exit 0 = OK para commit. Exit 1 = corrigir antes.
   ```
3. **Alternativas incorretas devem ser plausíveis e do mesmo domínio temático.** Proibido: distratores de outras disciplinas (ex.: "literatura brasileira" em questão de CIE), absolutismos óbvios isolados (`somente X`, `apenas Y`) quando a correta usa linguagem moderada, absurdos caricatos (`aumentam a cor da mangueira`, `oferecer bebida alcoólica`).
4. **Distratores por domínio:**
   - Legislação (CTB, IG): troca de prazo, competência, penalidade, definição, exceção, condição, artigo, ordem de procedimento.
   - APH/CBMSC: técnicas incorretas mas de APH (ex.: sequência errada, condição errada); nunca inventar protocolos absurdos.
   - CIE: equipamentos, classes, métodos — sempre dentro do Manual CIE.
5. **Alternativa correta não deve ser sistematicamente a mais longa.** Se a resposta técnica correta for necessariamente mais longa, normalizá-la tanto quanto possível sem perder precisão.

### 🔴 Shuffle e Rebalanceamento

Para rebalancear gabaritos após criar novas questões:
```bash
python3 scripts/auditoria_gabaritos.py --shuffle --seed 42 --write
python3 scripts/auditoria_gabaritos.py --audit  # confirmar exit 0
```

O seed 42 é padrão. Para criar variação numa nova rodada, use outro seed e documente em `Obsidian Vault/06 - Questões/Auditoria de Gabaritos e Qualidade das Questões.md`.

### 🟡 Estrutura do Vault

- **Não alterar notas atômicas** em `Obsidian Vault/03 - Tópicos Atômicos/` sem checagem explícita — são fontes de verdade para o conteúdo técnico.
- **Não alterar o Edital** em `Obsidian Vault/01 - Edital/` sem confirmar que a versão do arquivo PDF oficial foi verificada.
- **Não apagar conteúdo** sem registrar justificativa na nota de auditoria ou em commit mensagem.
- Templates estão em `Obsidian Vault/_Templates/`. Sempre usar `_Templates/Questão.md` ao criar questões novas.

### 🟡 Documentação

- Mudanças significativas devem ser registradas em `CHANGELOG.md` (seção `[Unreleased]`).
- Decisões arquiteturais vão em `docs/adr/ADR-NNN-titulo.md`.
- Status atual do projeto: `PROJECT_STATUS.md`.
- Handoff para a próxima sessão: `CONTINUITY.md`.

## Comandos Canônicos

```bash
# Auditoria completa (dry-run)
python3 scripts/auditoria_gabaritos.py --audit

# Rebalancear e salvar (seed reproduzível)
python3 scripts/auditoria_gabaritos.py --shuffle --seed 42 --write

# Auto-teste do script
python3 scripts/auditoria_gabaritos.py --self-test

# Ver relatório mais recente
ls -lt docs/relatorios/
```

## Estrutura de Arquivos Críticos

```
scripts/auditoria_gabaritos.py          # auditor + shuffler
docs/adr/ADR-001-auditoria-gabaritos.md # decisão arquitetural
docs/relatorios/                         # relatórios gerados pelo script
Obsidian Vault/06 - Questões/
  Simulado 01 - Diagnóstico.md          # 35q — auditado
  Simulado 02 - Conhecimentos Específicos.md  # 30q — auditado
  Simulado 03 - Reta Final.md           # 35q — auditado
  Gabaritos Comentados.md               # tabela consolidada (atualizada pelo script)
  Auditoria de Gabaritos e Qualidade das Questões.md  # esta auditoria
Obsidian Vault/_Templates/
  Questão.md                            # template com checklist anti-viés
  Simulado.md                           # template do contêiner
```

## O que NÃO fazer

- Não usar `git add -A` ou `git add .` sem verificar se há arquivos sensíveis ou binários grandes
- Não alterar `Gabaritos Comentados.md` manualmente (o script o sincroniza)
- Não criar questões sem usar o template `_Templates/Questão.md`
- Não ignorar exit code 1 do script de auditoria
- Não modificar seeds de shuffle sem documentar em `Auditoria de Gabaritos e Qualidade das Questões.md`

## Contexto da Última Auditoria

- **Data:** 2026-04-29
- **Distribuição pós-auditoria:** A=B=C=D=E=20% (100 questões)
- **Seed usado:** 42
- **Relatório:** `docs/relatorios/auditoria-gabaritos-2026-04-29.md`
- **ADR:** `docs/adr/ADR-001-auditoria-gabaritos.md`
