# Bombeiro Comunitário 2026 — v1.0.1

## Visão geral

Versão de correção metodológica, auditoria de fonte, simulados e aprimoramento
do guia de estudo. Mantém compatibilidade total com o vault v1.0.0.

---

## Destaques

### Auditoria do Manual CBAE — Nomenclatura oficial

O conteúdo CBAE foi auditado contra o `MANUAL_CBAE.pdf` (fonte oficial
primária). Foi identificado que o manual não usa ABCDE nem XABCDE como
protocolo estrutural. A nomenclatura oficial adotada pelo CBMSC é:

- **Avaliação da Cena**
- **Avaliação Geral da Vítima**

Sequência oficial (Manual CBAE, Lição IV, p. 98):
impressão geral → nível de consciência → vias aéreas + coluna cervical →
respiração → hemorragias graves.

### Distinção trauma × clínico formalizada

O manual distingue explicitamente (p. 108):
- Caso clínico → manobra de extensão de cabeça
- Trauma → manobra de empurre mandibular (assumir cervical em todo trauma)

### Torniquete marcado como técnica avançada

O Manual CBAE afirma literalmente (p. 118) que torniquete é técnica avançada e
não é ensinado como conduta básica no CBAE. As notas e flashcards foram
atualizados para refletir isso.

### XABCDE não introduzido

XABCDE não tem respaldo em nenhuma fonte oficial do projeto (edital, Manual
CBAE, IG 10-03-BM, Manual CIE). Não foi introduzido como conteúdo principal.

### Guia de estudo eficiente

Criado `docs/guia-de-estudo-eficiente.md` com:
- rotina diária recomendada
- hierarquia de fonte obrigatória
- rotinas por tempo disponível (30 min / 1h / 2h / 3h)
- seção específica sobre nomenclatura CBAE
- checklist diário

### Simulados estilo Instituto Fucap

Criada camada de simulados autorais baseada no edital:

- `Simulado 01 - Diagnóstico` — 35 questões.
- `Simulado 02 - Conhecimentos Específicos` — 30 questões.
- `Simulado 03 - Reta Final` — 35 questões.
- `Gabaritos Comentados`.
- `Matriz de Desempenho`.

As questões seguem o edital: 5 alternativas, uma correta, tema, fonte,
comentário e nota relacionada para revisão.

### Auditorias por disciplina

Criados relatórios de auditoria para edital, Português, Trânsito, CIE, CBAE e
IG 10-03-BM, registrando fontes, cobertura, lacunas e decisões.

---

## Arquivos criados

| Arquivo | Descrição |
|---|---|
| `docs/guia-de-estudo-eficiente.md` | Guia completo de uso eficiente |
| `docs/auditoria-edital.md` | Auditoria do edital |
| `docs/auditoria-portugues.md` | Auditoria de Português |
| `docs/auditoria-transito.md` | Auditoria de Trânsito |
| `docs/auditoria-cie.md` | Auditoria de CIE |
| `docs/auditoria-cbae.md` | Auditoria de CBAE |
| `docs/auditoria-ig-10-03-bm.md` | Auditoria da IG 10-03-BM |
| `docs/simulados-fucap.md` | Metodologia dos simulados |
| `docs/auditoria-protocolo-aph.md` | Relatório de auditoria CBAE |
| `Obsidian Vault/06 - Questões/Simulado 01 - Diagnóstico.md` | Simulado geral |
| `Obsidian Vault/06 - Questões/Simulado 02 - Conhecimentos Específicos.md` | Simulado específico |
| `Obsidian Vault/06 - Questões/Simulado 03 - Reta Final.md` | Simulado de reta final |
| `Obsidian Vault/06 - Questões/Gabaritos Comentados.md` | Correção consolidada |
| `Obsidian Vault/06 - Questões/Matriz de Desempenho.md` | Controle de desempenho |
| `Obsidian Vault/08 - Resumos Estratégicos/Avaliação Geral da Vítima vs ABCDE e XABCDE.md` | Nota estratégica com trechos literais do manual |
| `RELEASE_NOTES_v1.0.1.md` | Este arquivo |

## Arquivos alterados

| Arquivo | Alteração |
|---|---|
| `CBAE - Avaliação da Cena e Segurança.md` | Reescrito com "Avaliação Geral da Vítima" como eixo |
| `CBAE - Lição IV - Noções de Primeiros Socorros.md` | Nomenclatura oficial; ABCDE complementar |
| `CBAE - Hemorragia e Estado de Choque.md` | Torniquete marcado como técnica avançada |
| `CBAE - Vias Aéreas e Ventilação.md` | Distinção trauma × clínico formalizada |
| `CBAE - Intoxicação e Envenenamento.md` | ABCDE substituído pela sequência oficial |
| `CBAE - Índice Geral.md` | Referência atualizada |
| `Primeiros Socorros no Trânsito.md` | "ABCDE do trauma" removido; sequência CBAE |
| `Deck Emergências.md` | Bloco reescrito; cards novos sobre distinção trauma/clínico |
| `Deck Trânsito.md` | Card ABCDE substituído pela sequência CBAE |
| `Pegadinhas Fucap.md` | Pegadinhas CBAE atualizadas |
| `Erros - CBAE.md` | 3 registros de erro atualizados/adicionados |
| `Atendimento Básico (CBAE).md` | Descrições de links atualizadas |
| `README.md` | Links para guia de estudo e nota de auditoria |
| `docs/index.md` | Links para guia, simulados e auditorias |
| `docs/como-usar.md` | Fluxo com simulados |
| `docs/fluxo-de-estudo.md` | Referência ao guia completo e simulados |
| `docs/sistema-de-erros.md` | Modelo de erro de simulado |
| `CHANGELOG.md` | Entrada v1.0.1 |
| `PROJECT_STATUS.md` | Status atualizado |

---

## Observações técnicas

- O arquivo `Transporte de Urgência e Emergência.md` tinha modificação
  pré-existente de formatação YAML (não relacionada à auditoria) — não incluído
  neste release.
- Não foi criada tag `v1.0.1` automaticamente. Criar manualmente apenas após confirmação.
- GitHub Pages aguarda rebuild automático após push.

---

## Como criar a tag após conferência

```bash
git tag v1.0.1 -m "v1.0.1 — CBAE audit and study guide"
git push origin v1.0.1
```

Execute apenas após revisar o resultado no GitHub Pages.
