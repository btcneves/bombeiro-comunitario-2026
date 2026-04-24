---
tipo: índice-revisões
criado: 2026-04-24
tags: [revisão, spaced-repetition]
---

# Índice de Revisões

## Hoje

```dataview
TABLE disciplina, subtópico, incidência, ciclo-revisão AS "Ciclo", nível-domínio AS "Domínio"
FROM "03 - Tópicos Atômicos"
WHERE próxima-revisão = date(today)
SORT incidência DESC, dificuldade DESC
```

## Atrasadas

```dataview
TABLE disciplina, subtópico, próxima-revisão, ciclo-revisão AS "Ciclo"
FROM "03 - Tópicos Atômicos"
WHERE próxima-revisão < date(today)
SORT próxima-revisão ASC
```

## Próximos 7 Dias

```dataview
TABLE disciplina, subtópico, próxima-revisão
FROM "03 - Tópicos Atômicos"
WHERE próxima-revisão > date(today) AND próxima-revisão <= date(today) + dur(7 days)
SORT próxima-revisão ASC
```

## Regra Operacional

- Estudo inicial: `ciclo-revisão: 0`, `nível-domínio: 0`, `próxima-revisão: D+1`
- Revisão 1: atualizar `última-revisão` e mover `próxima-revisão` para `D+7`
- Revisão 2: mover para `D+30`
- Revisão 3: marcar `nível-domínio: 3` quando o conteúdo estiver estável

## Atalhos

- [[🎯 Dashboard]]
- [[Revisão Diária]]
- [[_Índice de Erros]]
