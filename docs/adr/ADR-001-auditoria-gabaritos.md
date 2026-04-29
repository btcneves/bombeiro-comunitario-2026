# ADR-001 — Auditoria de Gabaritos e Qualidade das Questões

**Status:** Aceito  
**Data:** 2026-04-29  
**Autor:** btcneves + Claude Code (Sonnet 4.6)

---

## Contexto

O banco de 100 questões dos Simulados 01, 02 e 03 do BC 2026 apresentava concentração crítica do gabarito na letra B: 56% das respostas corretas (B=56%, A=25%, C=13%, D=5%, E=1%). Adicionalmente, 65% das questões tinham a alternativa correta como a mais longa em caracteres, e muitas alternativas incorretas usavam absolutismos óbvios (`somente`, `apenas`, `nunca`) em oposição à linguagem institucional moderada da correta (`conforme`, `entre outros`, `quando possível`). Estes padrões permitem "chute sistemático" sem domínio do conteúdo.

O repositório não possui código de geração automática de questões — todas são elaboradas manualmente em Markdown. Portanto, o problema é **editorial/processual**, não de software.

## Causas Identificadas

1. **Ausência de salvaguarda de distribuição**: nenhum template, checklist ou ferramenta automatizada existia para alertar sobre concentração de gabarito.
2. **Ausência de contrato de agente**: sem `AGENTS.md`/`CLAUDE.md`, agentes assistidos por IA podiam gerar questões sem restrições editoriais.
3. **Viés cognitivo natural**: ao redigir questões isoladamente, a alternativa correta tende a ser mais longa (precisa ser completa e precisa) e a ocupar posições centrais (B, C) que parecem "neutras".
4. **Distratores de esforço mínimo**: alternativas incorretas escritas rapidamente tendem para absolutismos (`somente X`, `apenas Y`) por serem fáceis de formular como erradas.

## Decisão

Adotar três camadas de controle permanente:

### Camada 1 — Script de auditoria (`scripts/auditoria_gabaritos.py`)

Script Python 3 stdlib puro com dois modos:
- `--audit`: parseia todos os simulados e gera relatório Markdown + JSON em `docs/relatorios/`. Exit code 1 se alguma letra ≥30%, alternativa vazia/duplicada, gabarito inexistente ou campo Fonte/Comentário ausente.
- `--shuffle --seed N --write`: rebalanceia alternativas usando distribuição exata de 20% por letra (seed reproduzível), preserva o conteúdo da resposta correta por hash SHA-1, atualiza `Gabaritos Comentados.md`.

### Camada 2 — Templates com checklist (`_Templates/Questão.md` e `_Templates/Simulado.md`)

Templates Templater com checklist anti-viés embutido, exigindo execução do `--audit` antes de salvar, verificação de comprimento de alternativas e uso de distratores do mesmo domínio.

### Camada 3 — Contrato de agente (`AGENTS.md`)

Arquivo na raiz com regras obrigatórias para qualquer agente (Claude, Codex, ChatGPT, Cursor) que interaja com o repositório, incluindo proibição de criar questões sem balanceamento de gabaritos.

## Alternativas Consideradas

| Alternativa | Motivo de rejeição |
|---|---|
| Reescrita manual sem ferramenta | Não previne regressão; próxima sessão de estudo pode criar questões enviesadas |
| Embaralhamento aleatório puro (sem seed) | Não reproduzível; impossível verificar em auditoria |
| Reescrita completa dos simulados | Risco de perda de conteúdo técnico correto; desnecessário — o viés é posicional, não de conteúdo |
| Reordenação das questões (não das alternativas) | Não resolve o viés de letra do gabarito |

## Consequências

**Positivas:**
- Distribuição A=B=C=D=E=20% após aplicação do shuffle com seed 42.
- Distratores absurdos (`na alternativa mais extensa`, `oferecer bebida alcoólica`, `literatura brasileira` em contexto CIE) substituídos por alternativas plausíveis do mesmo domínio.
- Processo auditável e reproduzível: `python3 scripts/auditoria_gabaritos.py --self-test && --audit`.
- Script detecta regressão automaticamente (exit 1 = problema).

**Neutras/Trade-offs:**
- "Correta = mais longa" caiu de 65% para 58%. Os 58% restantes são questões onde a resposta técnica completa é genuinamente mais extensa — aceitar como inevitável.
- Seed 42 fixa o embaralhamento; para gerar variação, usar seeds diferentes em futuras rodadas.

**Atenção:**
- O shuffle reordena alternativas, preservando o conteúdo. A marca `**Gabarito:** X` aponta para o conteúdo correto original — nunca alterar manualmente o gabarito sem reordenar as alternativas correspondentemente.
- `Gabaritos Comentados.md` é atualizado automaticamente pelo script; edição manual pode dessincronizar.

## Como Reverter

```bash
git log --oneline  # encontrar commit pré-auditoria
git show <hash>:"Obsidian Vault/06 - Questões/Simulado 01 - Diagnóstico.md" > /tmp/sim01_orig.md
# repetir para Sim02, Sim03, Gabaritos Comentados.md
```

## Referências

- `scripts/auditoria_gabaritos.py` — implementação
- `docs/relatorios/auditoria-gabaritos-2026-04-29.md` — relatório da rodada inicial
- `Obsidian Vault/06 - Questões/Auditoria de Gabaritos e Qualidade das Questões.md` — nota no Vault
- `AGENTS.md` — contrato de agente
