# Roadmap

## Concluído

### v1.0.0 — Vault e documentação

- Vault consolidado como núcleo do projeto.
- Metodologia, arquitetura e operação documentadas.
- Repositório preparado para publicação no GitHub.

### v1.0.1 — Auditoria e simulados

- Edital e disciplinas auditados contra fontes oficiais.
- Simulados estilo provável da banca Instituto Fucap.
- Gabaritos comentados e matriz de desempenho.
- Guia de estudo eficiente.
- Release `v1.0.1` consolidada no Git.

### v1.1 — Diagramas e imagens

- Diagramas de arquitetura do vault.
- Fluxo de estudo completo.
- Ciclo de melhoria.
- Hierarquia de fidelidade ao edital.
- Pasta de imagens preparada para screenshots reais.

### v1.2 — Integração com Anki

- Fluxo de exportação seletiva documentado.
- Diferença entre Obsidian e Anki formalizada.
- Padrão de cards e cuidados contra duplicação documentados.

### v1.3 — Simulados avançados

- Plano de simulados no vault.
- Checklist pós-simulado.
- Guia de simulados avançados.
- Interpretação por faixas de desempenho.

### v1.4 — GitHub Pages

- `docs/index.md` consolidado como landing page.
- Configuração Jekyll em `docs/_config.yml`.
- Documentação pública reorganizada.

### v2.0 — Sistema adaptável para múltiplos concursos

- Processo de adaptação documentado.
- Checklist prático para novo concurso.
- Separação clara entre metodologia replicável e conteúdo específico.

### v1.5 — Auditoria de Gabaritos (concluído 2026-04-29)

- Script `scripts/auditoria_gabaritos.py` com modos `--audit`, `--shuffle`, `--self-test`.
- Rebalanceamento dos 3 simulados: B=56% → A=B=C=D=E=20% (seed 42).
- Reescrita de 15+ distratores absurdos/caricatos.
- Templates `_Templates/Questão.md` e `_Templates/Simulado.md` com checklist anti-viés.
- `AGENTS.md` — contrato para agentes AI.
- `docs/adr/ADR-001-auditoria-gabaritos.md`.
- Nota de auditoria no Vault.

## Roadmap futuro

- Adicionar screenshots reais do Obsidian.
- Automatizar exportação seletiva para Anki.
- Gerar simulados programaticamente a partir de banco estruturado.
- Validar links Markdown e wikilinks automaticamente.
- Criar CI simples para Markdown com `python3 scripts/auditoria_gabaritos.py --audit` como check.
- Adicionar provas anteriores FUCAP se fontes públicas forem localizadas.
- Reduzir "correta = mais longa" abaixo de 30% por normalização de comprimento.
- Hook de pré-commit para `--audit`.
