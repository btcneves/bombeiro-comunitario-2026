# Continuidade

## Estado atual

- Data: 2026-04-27.
- Branch: `main`.
- HEAD confirmado: `43ba149`.
- `main` sincronizada com `origin/main` no momento do diagnóstico.
- `git status --short`: limpo.
- Tags locais existentes: `v1.0.0`, `v1.0.1`.
- Vault Obsidian preservado.
- PDFs oficiais preservados.
- Vault validado com 125 arquivos Markdown e 0 wikilinks quebrados.
- Release GitHub `v1.0.1`: não confirmada localmente por falha de conexão com `api.github.com`.

## Sem pendência local crítica

A versão `v1.0.1` já existe no Git. Não há pendência local crítica para essa
versão. A próxima missão é fechar o roadmap atual e preparar a versão `v1.1.0`
como consolidação madura do projeto.

## Próximos blocos de trabalho

1. Diagramas e imagens:
   - arquitetura do vault;
   - fluxo de estudo completo;
   - ciclo de melhoria;
   - fidelidade ao edital;
   - placeholder documental para screenshots reais.

2. Integração Anki:
   - guia `docs/integracao-anki.md`;
   - README dos decks em `Obsidian Vault/04 - Flashcards/README.md`;
   - links em README, docs/index e docs/flashcards.

3. Simulados avançados:
   - guia `docs/simulados-avancados.md`;
   - `Plano de Simulados.md`;
   - `Checklist Pós-Simulado.md`;
   - integração com matriz de desempenho e banco de questões.

4. GitHub Pages consolidado:
   - `docs/index.md` como landing page final;
   - `docs/_config.yml` para Jekyll;
   - link inferido: `https://btcneves.github.io/bombeiro-comunitario-2026/`.

5. Documentação final:
   - README final profissional;
   - roadmap concluído;
   - changelog `1.1.0`;
   - release notes `RELEASE_NOTES_v1.1.0.md`;
   - portfolio atualizado.

## Auditoria de Gabaritos — concluída em 2026-04-29

A concentração de gabarito em B (56%) foi detectada e corrigida. Estado atual:

- Distribuição: A=B=C=D=E=20% (100 questões)
- Script de auditoria: `scripts/auditoria_gabaritos.py`
- Exit code na última rodada: 0 (sem violações)
- Seed de embaralhamento: 42
- Contrato de agente: `AGENTS.md`
- Nota no Vault: `Obsidian Vault/06 - Questões/Auditoria de Gabaritos e Qualidade das Questões.md`

## Pendências em aberto

- "Correta = mais longa" ainda em 58% — redução futura por normalização de comprimento ao criar novas questões.
- Simulado 04 ainda não criado — usar `_Templates/Simulado.md` quando criar.
- Hook de pré-commit para `--audit` não configurado ainda.

## Próximo comando recomendado

```bash
# Verificar estado da auditoria
python3 scripts/auditoria_gabaritos.py --audit

# Verificar git
git status --short
```
