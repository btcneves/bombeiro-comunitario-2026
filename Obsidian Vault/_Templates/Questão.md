---
id: <% tp.system.prompt("ID (ex.: S01-Q14)") %>
disciplina: <% tp.system.prompt("Disciplina") %>
tema: <% tp.system.prompt("Tema") %>
nivel: <% tp.system.prompt("Nível: Fácil | Médio | Difícil") %>
tipo: <% tp.system.prompt("Tipo: Literal | Aplicação | Interpretação | Pegadinha") %>
criado: <% tp.date.now("YYYY-MM-DD") %>
tags: [questão]
---

### Questão <% tp.system.prompt("Número") %>

**Disciplina:** <% tp.frontmatter.disciplina %>
**Tema:** <% tp.frontmatter.tema %>
**Nível:** <% tp.frontmatter.nivel %>
**Tipo:** <% tp.frontmatter.tipo %>

_Enunciado da questão aqui._

A) alternativa um  
B) alternativa dois  
C) alternativa três  
D) alternativa quatro  
E) alternativa cinco

**Gabarito:** X
**Comentário:** _Justificativa baseada na fonte oficial._
**Fonte:** _Lei/Manual/Artigo específico._
**Revisar:** [[]]

---

## Checklist anti-viés (preencher antes de salvar)

- [ ] Gabarito não é sempre B — conferir distribuição do simulado com `python3 scripts/auditoria_gabaritos.py --audit`
- [ ] Alternativa correta NÃO é a mais longa (ou se for, há justificativa técnica inevitável)
- [ ] Nenhum distrator usa absolutismo óbvio (`somente`, `apenas`, `nunca`) enquanto a correta usa linguagem moderada
- [ ] Distratores são do mesmo domínio temático (sem alternativas de outras disciplinas)
- [ ] Alternativas não estão duplicadas
- [ ] Campo `Fonte` tem referência específica (lei + artigo, ou manual + lição)
- [ ] Campo `Comentário` explica POR QUE a correta é correta E por que as erradas são erradas
- [ ] Em questões de APH/CBMSC: distratores não inventam protocolos absurdos; usam erros plausíveis de troca de sequência, condição ou competência
- [ ] Em questões de legislação: distratores usam troca de prazo, penalidade, competência, definição, exceção, condição, artigo ou ordem de procedimento
