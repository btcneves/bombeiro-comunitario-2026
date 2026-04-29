# Changelog

## [Unreleased] — Auditoria de Gabaritos 2026-04-29

### Added

- Script `scripts/auditoria_gabaritos.py` — auditor + shuffler Python 3 stdlib puro com modos `--audit`, `--shuffle --seed N --write` e `--self-test`.
- `scripts/README.md` — instruções de uso.
- `docs/relatorios/auditoria-gabaritos-2026-04-29.md` + `.json` — relatório baseline e pós-shuffle.
- `docs/adr/ADR-001-auditoria-gabaritos.md` — decisão arquitetural sobre auditoria de gabaritos.
- `AGENTS.md` — contrato de agente para Claude/Codex/ChatGPT com regras anti-viés obrigatórias.
- `Obsidian Vault/06 - Questões/Auditoria de Gabaritos e Qualidade das Questões.md` — nota de registro no Vault.
- `Obsidian Vault/_Templates/Questão.md` e `Obsidian Vault/_Templates/Simulado.md` — templates com checklist anti-viés.

### Changed

- Simulados 01, 02 e 03: gabaritos rebalanceados de B=56% para A=B=C=D=E=20% (seed 42).
- Distratores absurdos substituídos por alternativas plausíveis do mesmo domínio em 15+ questões.
- `Obsidian Vault/06 - Questões/Gabaritos Comentados.md`: tabela atualizada automaticamente pelo script.
- `Obsidian Vault/06 - Questões/Plano de Simulados.md`: seção "Regras anti-viés" adicionada.
- `docs/simulados-fucap.md`: checklist anti-viés adicionado.
- `docs/simulados-avancados.md`: instrução de `--audit` antes de commit.
- `docs/integracao-anki.md`: nota sobre "shuffle answers" no Anki.

### Fixed

- Concentração crítica de gabarito em B (56% → 20%): corrigida por shuffle com seed reproduzível.
- "Alternativa correta = mais longa": melhorada de 65% → 58% por reescrita de distratores.
- Padrão absolutismo-em-erradas vs. hedge-na-correta: múltiplas alternativas reescritas.

---

## [1.1.0] - 2026-04-27

### Added

- Diagramas de arquitetura e fluxo.
- Guia de integração com Anki.
- Simulados avançados.
- Plano de simulados.
- Checklist pós-simulado.
- Checklist para adaptação a outros concursos.
- GitHub Pages consolidado.

### Changed

- README ampliado como apresentação final.
- Documentação pública reorganizada.
- Roadmap atualizado para refletir o estado real.
- Portfolio atualizado com a camada final de maturidade.

### Fixed

- Status da v1.0.1 atualizado em `PROJECT_STATUS.md` e `CONTINUITY.md`.
- Release notes v1.0.1 atualizadas para refletir tag já existente.

---

## [1.0.1] - 2026-04-27

### Added

- Guia de estudo eficiente (`docs/guia-de-estudo-eficiente.md`) com rotina
  diária, rotinas por tempo disponível, seção CBAE e checklist.
- Auditoria do edital e auditorias por disciplina.
- Três simulados no estilo provável da banca Instituto Fucap.
- Banco de questões expandido, gabaritos comentados e matriz de desempenho.
- Relatório de auditoria educacional (`docs/auditoria-protocolo-aph.md`) sobre
  protocolo de avaliação da vítima no CBAE, com trechos literais do Manual CBAE.
- Nota estratégica sobre Avaliação Geral da Vítima vs ABCDE/XABCDE no vault.
- Release notes v1.0.1.

### Changed

- Conteúdo CBAE alinhado à nomenclatura oficial do Manual CBAE: "Avaliação da
  Cena" e "Avaliação Geral da Vítima" passam a ser o eixo principal.
- Distinção trauma × clínico formalizada conforme p. 108 do manual: empurre
  mandibular (trauma) vs extensão de cabeça (caso clínico).
- Flashcards de emergências e trânsito corrigidos com a sequência oficial.
- Links de documentação atualizados para incluir guia de estudo eficiente.
- Documentação de simulados integrada ao README, docs e sistema de erros.
- PROJECT_STATUS e CHANGELOG atualizados.

### Fixed

- Remoção de ABCDE como resposta principal em conteúdo CBAE — mantido apenas
  como observação complementar.
- Remoção do rótulo "ABCDE do trauma" de nota de Trânsito.
- Torniquete marcado como técnica avançada conforme p. 118 do Manual CBAE, não
  como conduta básica de primeiros socorros.
- XABCDE não introduzido — ausência de respaldo nas fontes oficiais do projeto.
- Simulados ajustados ao formato real do edital: 5 alternativas e uma correta.

---

## [1.0.0] - 2026-04-24

### Added

- Estrutura inicial do repositório.
- Vault Obsidian para estudo do concurso.
- Documentação completa.
- Sistema de revisão espaçada.
- Flashcards e dashboard.
- Sistema de erros e resumos estratégicos.
