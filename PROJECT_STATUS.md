# Project Status

## Status geral

Projeto ativo, documentado e em estado maduro de publicação pública.

## Snapshot atual

- Data: `2026-04-27`
- Branch: `main`
- HEAD: `43ba149`
- Remote: `origin/main` sincronizado no mesmo commit
- Git status: limpo
- Release atual no Git: `v1.0.1`
- Tags locais confirmadas: `v1.0.0`, `v1.0.1`
- Release GitHub `v1.0.1`: não confirmada localmente por falha de conexão com `api.github.com`
- Simulados criados: `3`
- Questões autorais criadas: `100`
- Vault Obsidian: `125` arquivos Markdown
- Wikilinks quebrados no vault: `0`
- PDFs e fontes oficiais preservados

## v1.0.1 concluída no Git

A versão `v1.0.1` está consolidada no histórico local e associada ao commit
`43ba149`. Ela inclui auditorias, guia de estudo eficiente, simulados estilo
Instituto Fucap, gabaritos comentados, matriz de desempenho e documentação
pública atualizada.

## Auditoria educacional concluída

- Fonte primária auditada: `MANUAL_CBAE.pdf` (pdftotext, Lição IV, pp. 97-120)
- Resultado: Manual CBAE não usa ABCDE/XABCDE como eixo estrutural
- Nomenclatura oficial adotada: "Avaliação da Cena" e "Avaliação Geral da Vítima"
- Distinção trauma x clínico formalizada conforme p. 108 do manual
- Torniquete marcado como técnica avançada conforme p. 118
- XABCDE não introduzido como conteúdo principal
- Relatório: `docs/auditoria-protocolo-aph.md`
- Nota estratégica: `Obsidian Vault/08 - Resumos Estratégicos/Avaliação Geral da Vítima vs ABCDE e XABCDE.md`

## Componentes presentes

- Dashboard central com consultas Dataview.
- Edital e materiais-base organizados.
- Disciplinas mapeadas.
- Tópicos atômicos com frontmatter padronizado.
- Decks de flashcards por disciplina.
- Índices de revisão e de erros.
- Banco de questões com 3 simulados e 100 questões.
- Gabaritos comentados e matriz de desempenho.
- Resumos estratégicos e templates operacionais.
- Guia de estudo eficiente com rotinas por tempo disponível.
- Relatórios de auditoria educacional e por disciplina.

## Integridade

- O `Obsidian Vault` foi preservado como ambiente operacional do projeto.
- A documentação pública cobre uso, metodologia, arquitetura, fontes e aviso
  institucional.
- Todo o conteúdo CBAE auditado está alinhado ao Manual CBAE oficial.
- Simulados seguem o edital: 5 alternativas, uma correta e conteúdo dentro do
  programa.
- Em caso de divergência entre resumos e materiais-base, prevalecem as fontes
  oficiais (edital -> apostila oficial -> manual CBMSC).

## Consolidação v1.1.0

O roadmap atual foi consolidado em documentação e arquivos de apoio:
diagramas, integração Anki, simulados avançados, GitHub Pages, adaptação para
outros concursos e release notes `v1.1.0`.

## Auditoria de Gabaritos — 2026-04-29

Problema detectado e corrigido: concentração crítica do gabarito em B (56%).

- **Distribuição pós-auditoria:** A=B=C=D=E=20% (100 questões)
- **Script:** `scripts/auditoria_gabaritos.py` (audit/shuffle/self-test)
- **Seed:** 42 (reproduzível)
- **Distratores reescritos:** 15+ questões com alternativas absurdas substituídas
- **Relatório:** `docs/relatorios/auditoria-gabaritos-2026-04-29.md`
- **ADR:** `docs/adr/ADR-001-auditoria-gabaritos.md`
- **Contrato de agente:** `AGENTS.md`
- **Nota Vault:** `Obsidian Vault/06 - Questões/Auditoria de Gabaritos e Qualidade das Questões.md`
- **Status:** ✅ Exit 0 — sem violações bloqueantes
