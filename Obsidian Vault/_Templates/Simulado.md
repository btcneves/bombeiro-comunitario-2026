---
tipo: simulado
criado: <% tp.date.now("YYYY-MM-DD") %>
questoes: <% tp.system.prompt("Total de questões") %>
tags: [simulado, fucap]
---

# Simulado <% tp.system.prompt("Número e título (ex.: 04 - Reforço CIE)") %>

**Objetivo:** <% tp.system.prompt("Objetivo do simulado") %>
**Formato:** <% tp.frontmatter.questoes %> questões, 5 alternativas, uma correta.

> **Antes de salvar:** executar `python3 scripts/auditoria_gabaritos.py --audit`
> A auditoria deve retornar exit 0 (todas as letras ≤ 25% e sem alternativas vazias/duplicadas).

---

_Cole as questões aqui seguindo o template `Questão.md`. Cada questão deve conter:_
_`### Questão NN`, **Disciplina**, **Tema**, **Nível**, **Tipo**, enunciado, alternativas A–E, **Gabarito**, **Comentário**, **Fonte**, **Revisar**._

---

## Gabarito Rápido

| Q | Gabarito | Tema | Revisar |
|---:|:---:|---|---|
| 01 | — | | |
| 02 | — | | |

> Após finalizar as questões, rode `--audit` para confirmar a distribuição e copie a tabela para `[[Gabaritos Comentados]]`.

## Conexões

- [[_Banco de Questões]]
- [[Gabaritos Comentados]]
- [[Plano de Simulados]]
- [[Checklist Pós-Simulado]]
- [[Matriz de Desempenho]]
