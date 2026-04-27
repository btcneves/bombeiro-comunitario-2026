# Arquitetura do Vault

Este diagrama mostra a arquitetura operacional do vault, da fonte oficial ao
painel diário de estudo.

```mermaid
flowchart LR
    A[Edital] --> B[Disciplinas]
    B --> C[Tópicos Atômicos]
    C --> D[Flashcards]
    C --> E[Questões]
    E --> F[Erros]
    F --> G[Revisão]
    D --> G
    G --> H[Dashboard]
    H --> B
```

## Leitura

O edital define o escopo. As disciplinas organizam o conteúdo, os tópicos
atômicos transformam esse conteúdo em unidades revisáveis, e flashcards,
questões, erros e revisão fecham o ciclo de domínio.
