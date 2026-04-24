---
tipo: dashboard
criado: 2026-04-24
---

# 🎯 Dashboard — Bombeiro Comunitário Imaruí 2026

> **Prova**: 03/05/2026 | **Físico**: 13-14/06/2026 | **Mínimo**: 5,0/10

---

## ⏰ Contagem Regressiva

```dataview
TABLE WITHOUT ID
  ("**" + (date("2026-05-03") - date(today)).days + " dias para a prova**") AS "Prazo"
```

---

## 📊 Progresso por Disciplina

```dataview
TABLE
  round((sum(rows.nível-domínio) / (length(rows) * 3)) * 100, 1) + "%" AS "% Real",
  length(filter(rows, (r) => r["nível-domínio"] = 3)) AS "✅ Dominado",
  length(filter(rows, (r) => r["nível-domínio"] = 2)) AS "🔄 Revisado",
  length(filter(rows, (r) => r["nível-domínio"] <= 1)) AS "⚠️ Fracos",
  length(rows) AS "Total"
FROM "03 - Tópicos Atômicos"
WHERE disciplina
GROUP BY disciplina
SORT disciplina ASC
```

---

## 📅 Revisões para Hoje

```dataview
TABLE disciplina, subtópico, incidência, ciclo-revisão AS "Ciclo", nível-domínio AS "Domínio"
FROM "03 - Tópicos Atômicos"
WHERE próxima-revisão = date(today)
SORT incidência DESC
```

---

## ⏳ Revisões Atrasadas

```dataview
TABLE disciplina, subtópico, próxima-revisão, ciclo-revisão AS "Ciclo"
FROM "03 - Tópicos Atômicos"
WHERE próxima-revisão < date(today)
SORT próxima-revisão ASC, incidência DESC
```

---

## 🔴 Prioridade Máxima — Alta Incidência Não Dominadas

```dataview
TABLE disciplina, subtópico, dificuldade, nível-domínio AS "Domínio", próxima-revisão AS "Revisão"
FROM "03 - Tópicos Atômicos"
WHERE incidência = "🔴" AND nível-domínio < 3
SORT nível-domínio ASC, dificuldade DESC, próxima-revisão ASC
LIMIT 15
```

---

## 📉 Pontos Fracos

```dataview
TABLE disciplina, subtópico, dificuldade, status, última-revisão
FROM "03 - Tópicos Atômicos"
WHERE nível-domínio <= 1
SORT incidência DESC, dificuldade DESC
LIMIT 20
```

---

## 📋 Checklist do Edital

- [ ] #tarefa Língua Portuguesa — 16 tópicos revisados 📅 2026-05-02
- [ ] #tarefa CTB / Legislação de Trânsito — 15 blocos revisados 📅 2026-05-01
- [ ] #tarefa Manual CIE — lições 1-6 revisadas 📅 2026-04-29
- [ ] #tarefa Manual CBAE — lições 1-4 revisadas 📅 2026-04-30
- [ ] #tarefa IG 10-03-BM — caps. I-XIX revisados 📅 2026-04-29
- [ ] #tarefa Simulado completo #1 📅 2026-04-30
- [ ] #tarefa Simulado completo #2 📅 2026-05-01
- [ ] #tarefa Revisão geral — flashcards críticos 📅 2026-05-02

---

## 🕐 Todas as Notas — Tabela Geral

```dataview
TABLE disciplina, subtópico, incidência, status, próxima-revisão AS "Próxima Revisão"
FROM "03 - Tópicos Atômicos"
WHERE disciplina
SORT incidência DESC, status ASC
```

---

## 🚨 Erros Recentes

```dataview
TABLE disciplina, tópico-erro AS "Tópico", data-erro AS "Data"
FROM "09 - Erros e Aprendizados"
WHERE tipo = "erro"
SORT data-erro DESC
LIMIT 10
```

---

## 🔗 Atalhos Rápidos

| Seção | Link |
|-------|------|
| Cronograma 9 dias | [[📅 Cronograma 9 Dias]] |
| Preparação Física | [[🏃 Preparação Física]] |
| Edital Completo | [[Edital Completo]] |
| Língua Portuguesa | [[Língua Portuguesa]] |
| Legislação de Trânsito | [[Legislação de Trânsito]] |
| Combate a Incêndio | [[Combate a Incêndio (CIE)]] |
| Atendimento Básico | [[Atendimento Básico (CBAE)]] |
| Serviço Comunitário | [[Serviço Comunitário (IG 10-03-BM)]] |
| Banco de Questões | [[_Banco de Questões]] |
| Índice de Erros | [[_Índice de Erros]] |
| Resumo Brutal — Trânsito | [[Resumo Brutal - Trânsito]] |
| Resumo Brutal — Português | [[Resumo Brutal - Português]] |
| Pegadinhas Fucap | [[Pegadinhas Fucap]] |
