---
disciplina: <% tp.system.prompt("Disciplina") %>
tópico: <% tp.system.prompt("Tópico") %>
tipo: erro
data: <% tp.date.now("YYYY-MM-DD") %>
fonte: <% tp.system.prompt("Fonte (simulado/revisão/prova)") %>
status: pendente
tags: [erro]
---

# Erro — <% tp.file.title %>

## ❌ O que eu errei
> Transcreva a questão ou descreva o erro cometido.



## 🔍 Por que errei
> Lacuna de conhecimento, confusão de conceito, pegadinha?



## ✅ Resposta correta
> Conceito correto, com justificativa.



## 🔗 Nota de referência
[[]]

## 🃏 Flashcard de reforço
#flashcards

Qual o erro que cometi sobre <% tp.file.title %>?
?
Descreva a resposta correta aqui.

