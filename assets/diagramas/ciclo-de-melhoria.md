# Ciclo de Melhoria

O projeto usa erro, revisão e simulado como mecanismos de melhoria contínua.

```mermaid
flowchart LR
    A[Estudar] --> B[Testar]
    B --> C[Errar]
    C --> D[Registrar]
    D --> E[Corrigir]
    E --> F[Revisar]
    F --> G[Simular]
    G --> H[Medir desempenho]
    H --> A
```

## Leitura

O erro não encerra o ciclo. Ele vira registro, correção, revisão e novo teste
até aparecer melhora mensurável na matriz de desempenho.
