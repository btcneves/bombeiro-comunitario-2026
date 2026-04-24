---
data: <% tp.date.now("YYYY-MM-DD") %>
tipo: revisão-diária
horas-estudadas: 0
humor: 
tags: [diário]
---

# Revisão Diária — <% tp.date.now("DD/MM/YYYY") %>

## 📋 Tópicos para revisar hoje

```dataview
TABLE disciplina, status, dificuldade
FROM "03 - Tópicos Atômicos"
WHERE próxima-revisão = date("<% tp.date.now("YYYY-MM-DD") %>")
SORT disciplina ASC
```

## 🎯 Foco do dia
> O que você vai estudar hoje (além das revisões acima)?



## ✅ O que foi feito
- [ ] 
- [ ] 
- [ ] 

## ❌ Erros do dia
> Cole aqui os erros cometidos ou crie notas em [[_Índice de Erros]].



## 📊 Métricas
- Horas estudadas: 
- Questões resolvidas: 
- Taxa de acerto: 

## 💭 Observação do dia

