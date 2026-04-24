# Arquitetura

## Visão geral

O projeto foi estruturado como um sistema de estudo em camadas. Cada pasta do
vault tem função operacional clara, evitando mistura entre fonte, síntese,
prática e revisão.

## Estrutura principal

### `00 - Dashboard`

Centro operacional do vault. Reúne indicadores, revisões do dia, prioridades,
atrasos, checklist do edital e atalhos rápidos.

### `01 - Edital`

Camada de referência formal. Organiza o edital, cronograma oficial e
atribuições do cargo para manter o estudo alinhado à fonte de cobrança.

### `02 - Disciplinas`

Páginas centrais por disciplina. Funcionam como pontos de navegação e
organização do conteúdo macro.

### `03 - Tópicos Atômicos`

Núcleo do conhecimento. Cada nota representa um conceito, tema ou subtópico
com granularidade suficiente para revisão e conexão semântica.

### `04 - Flashcards`

Decks por disciplina e cards derivados das notas. É a camada de recuperação ativa.

### `05 - Revisões`

Índices e regras de revisão espaçada. Faz a leitura do frontmatter das notas
atômicas para exibir o que deve ser revisado.

### `06 - Questões`

Base para banco de questões e ligação entre cobrança prática e conhecimento estudado.

### `07 - Mapas Mentais`

Espaço reservado para representações visuais e sínteses gráficas de assuntos complexos.

### `08 - Resumos Estratégicos`

Camada de condensação de alta utilidade para reta final, revisão rápida e identificação de pegadinhas.

### `09 - Erros e Aprendizados`

Sistema de captura de falhas, causas-raiz e correções. Transforma desempenho
ruim em revisão dirigida.

### `_Templates`

Modelos operacionais para padronizar criação de nota atômica, erro, flashcard, revisão diária e resumo estratégico.

## Padrão de frontmatter

As notas atômicas seguem um frontmatter estrutural como este:

```yaml
disciplina:
tópico:
subtópico:
incidência:
status:
criado:
última-revisão:
próxima-revisão:
ciclo-revisão:
dificuldade:
nível-domínio:
tags:
```

## Função de cada campo

- `disciplina`: área macro do conteúdo.
- `tópico`: agrupador conceitual ou capítulo.
- `subtópico`: recorte específico da nota.
- `incidência`: prioridade ou recorrência percebida.
- `status`: estado atual do estudo.
- `criado`: data de criação da nota.
- `última-revisão`: última vez em que o tópico foi revisado.
- `próxima-revisão`: data-alvo da revisão seguinte.
- `ciclo-revisão`: etapa do ciclo espaçado.
- `dificuldade`: carga subjetiva ou técnica do tema.
- `nível-domínio`: maturidade do conhecimento.
- `tags`: marcações auxiliares.

## Escala de nível-domínio

- `0 = não estudado`
- `1 = visto`
- `2 = revisado`
- `3 = dominado`

## Como a arquitetura se integra

O fluxo esperado é:

1. o edital orienta o que precisa ser coberto
2. a disciplina organiza o mapa macro
3. a nota atômica concentra o conhecimento estudável
4. os flashcards exercitam recuperação
5. a revisão lê datas e prioridades
6. os erros realimentam o sistema
7. os resumos estratégicos servem à reta final

Essa separação mantém o vault utilizável no dia a dia e, ao mesmo tempo, documentável como sistema técnico.
