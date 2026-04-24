# Sistema de revisão

## Objetivo

O sistema de revisão existe para garantir que conteúdo estudado continue
recuperável ao longo do tempo. Ele depende do frontmatter das notas atômicas e
das consultas Dataview no dashboard e nos índices.

## Campos usados

- `última-revisão`
- `próxima-revisão`
- `ciclo-revisão`
- `nível-domínio`
- `disciplina`
- `subtópico`
- `incidência`

## Como atualizar a revisão manualmente

Após revisar uma nota:

1. preencha `última-revisão` com a data atual
2. avance `ciclo-revisão`
3. defina a nova `próxima-revisão`
4. ajuste `nível-domínio` conforme estabilidade real do conteúdo

## Como interpretar `próxima-revisão`

- data igual a hoje: revisar hoje
- data anterior a hoje: revisão atrasada
- data futura: tópico já programado

## Como usar Dataview

O Dataview lê o frontmatter das notas e monta tabelas automáticas, como:

- revisões para hoje
- revisões atrasadas
- pontos fracos
- prioridades por incidência e domínio

Sem preencher corretamente o frontmatter, o dashboard perde utilidade operacional.

## Como manter o ciclo `D+1`, `D+7`, `D+30`

Regra recomendada:

- estudo inicial: `ciclo-revisão: 0`, `nível-domínio: 0`, `próxima-revisão: D+1`
- revisão 1: mover para `D+7`
- revisão 2: mover para `D+30`
- revisão 3: reclassificar como dominado se o desempenho estiver estável

## Como mudar `nível-domínio`

- `0`: ainda não estudado de forma real
- `1`: conteúdo visto, mas frágil
- `2`: já revisado e parcialmente estável
- `3`: conteúdo dominado com boa recuperação

Não use `3` por sensação de familiaridade. Use quando o tópico realmente resistir a questão, flashcard e revisão.

## Exemplo de frontmatter antes da revisão

```yaml
disciplina: CIE
tópico: Combate a Incêndio Estrutural
subtópico: Fundamentos do Fogo
incidência: 🔴
status: em-estudo
criado: 2026-04-24
última-revisão:
próxima-revisão: 2026-04-25
ciclo-revisão: 0
dificuldade: 3
nível-domínio: 0
tags: [CIE, fogo, incêndio]
```

## Exemplo de frontmatter depois da revisão

```yaml
disciplina: CIE
tópico: Combate a Incêndio Estrutural
subtópico: Fundamentos do Fogo
incidência: 🔴
status: revisado
criado: 2026-04-24
última-revisão: 2026-04-25
próxima-revisão: 2026-05-02
ciclo-revisão: 1
dificuldade: 3
nível-domínio: 1
tags: [CIE, fogo, incêndio]
```

## Regra prática

Revisão boa não é só “li de novo”. Ela envolve tentar lembrar, responder,
errar pouco e atualizar o sistema para a próxima janela correta.
