# scripts/

Scripts de manutenção e auditoria do BC 2026. Python 3 stdlib puro — sem dependências externas.

## auditoria_gabaritos.py

Audita e rebalanceia os gabaritos dos simulados Markdown.

```bash
# Auditoria (dry-run, default)
python3 scripts/auditoria_gabaritos.py --audit

# Rebalancear e salvar em disco
python3 scripts/auditoria_gabaritos.py --shuffle --seed 42 --write

# Auto-teste
python3 scripts/auditoria_gabaritos.py --self-test
```

**Saída:** `docs/relatorios/auditoria-gabaritos-AAAA-MM-DD.md` + `.json`

**Exit codes:**
- `0` — sem violações (OK para commit)
- `1` — alguma letra ≥30%, alternativa vazia/duplicada, gabarito inválido ou campo obrigatório ausente

**Critérios de aprovação:**
- Cada letra A/B/C/D/E com ≤29% das questões por simulado
- Zero alternativas vazias ou duplicadas
- Zero gabaritos apontando para letra inexistente
- Zero questões sem Fonte ou sem Comentário

**Parâmetros:**
| Flag | Descrição |
|---|---|
| `--audit` | Modo auditoria (default, não modifica arquivos) |
| `--shuffle` | Modo embaralhamento (use `--write` para salvar) |
| `--seed N` | Seed para reproduzibilidade (default: 42) |
| `--write` | Salva arquivos modificados (só com `--shuffle`) |
| `--self-test` | Executa bateria interna de testes e sai |
| `--no-save-report` | Não gera arquivo de relatório |
