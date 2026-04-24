---
disciplina: <% tp.system.prompt("Disciplina") %>
tipo: flashcard
criado: <% tp.date.now("YYYY-MM-DD") %>
tags: [flashcard]
---

# Flashcards — <% tp.file.title %>

#flashcards

<!-- Formato cartão simples: -->
Pergunta::Resposta

<!-- Formato cartão multi-linha: -->
Pergunta longa
?
Resposta longa

<!-- Formato reverso (aparece dos dois lados): -->
Conceito:::Definição

