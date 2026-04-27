# Continuidade

## Estado atual

- Data: 2026-04-27.
- Branch esperada: `main`.
- Vault preservado.
- PDFs oficiais não foram alterados.
- Simulados e auditorias foram criados.
- Tag `v1.0.1` não deve ser criada sem confirmação do usuário.

## Fontes consultadas

- `Edital/EDITAL DE CONCURSO PUBLICO.pdf`
- `CONTEÚDO PROGRAMÁTICO/CONHECIMENTOS GERAIS/Língua Portuguesa.pdf`
- `CONTEÚDO PROGRAMÁTICO/CONHECIMENTOS ESPECÍFICOS/MANUAL_CBAE.pdf`
- `CONTEÚDO PROGRAMÁTICO/CONHECIMENTOS ESPECÍFICOS/MANUAL_CIE.pdf`
- `CONTEÚDO PROGRAMÁTICO/CONHECIMENTOS ESPECÍFICOS/IG 10-03-BM.pdf`
- `README.md`, `SOURCES.md`, `NOTICE.md`, `docs/`
- `Obsidian Vault/`

## Arquivos alterados ou criados

- Auditorias em `docs/auditoria-*.md`.
- Metodologia de simulados em `docs/simulados-fucap.md`.
- Simulados, gabaritos e matriz em `Obsidian Vault/06 - Questões/`.
- Integração do sistema de erros em `docs/sistema-de-erros.md` e `_Índice de Erros.md`.
- Atualizações públicas em `README.md`, `docs/`, `ROADMAP.md`,
  `PORTFOLIO.md`, `PROJECT_STATUS.md`, `CHANGELOG.md` e
  `RELEASE_NOTES_v1.0.1.md`.

## Simulados criados

- `Simulado 01 - Diagnóstico.md`: 35 questões.
- `Simulado 02 - Conhecimentos Específicos.md`: 30 questões.
- `Simulado 03 - Reta Final.md`: 35 questões.
- Total: 100 questões.

## Decisões metodológicas

- Edital e PDFs oficiais prevalecem.
- Simulados usam 5 alternativas, pois o edital define esse formato.
- CBAE usa Avaliação da Cena e Avaliação Geral da Vítima como nomenclatura oficial.
- ABCDE só aparece como observação complementar.
- XABCDE não é conteúdo principal.
- Torniquete é tratado como técnica avançada no contexto do Manual CBAE.

## Riscos

- Validar se todas as notas linkadas nos simulados existem no Obsidian.
- Conferir se a alteração local pré-existente em `Transporte de Urgência e Emergência.md`
  deve ser incluída no commit ou mantida separada.
- GitHub Pages só deve ser considerado atualizado após push e rebuild.

## Próximos comandos exatos

```bash
git status --short
git diff --stat
rg -ni "XABCDE|ABCDE|Avaliação Geral da Vítima" "Obsidian Vault" docs README.md
rg -ni "Instituto Fucap|FUCAP|simulado|gabarito" "Obsidian Vault" docs README.md
```

Depois, validar arquivos exigidos, fazer commits organizados e executar `git push`.
