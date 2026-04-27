# Integração com Anki

## Objetivo

A integração com Anki serve para transformar parte dos flashcards do Obsidian
em repetição intensiva externa, sem tirar do vault a função de fonte principal
do estudo.

O fluxo recomendado é:

```text
Obsidian como fonte -> revisão local -> exportação seletiva -> Anki para repetição intensiva
```

## Obsidian e Anki têm papéis diferentes

No Obsidian, os cards ficam próximos das notas, fontes, simulados e registros
de erro. Isso facilita contexto, correção e rastreabilidade.

No Anki, os cards ganham uma fila de revisão dedicada e mais rígida. Isso é
útil para repetição intensiva, especialmente em assuntos de memorização curta,
pegadinhas recorrentes e pontos errados em simulado.

## Formato atual

O projeto usa o padrão:

```text
Pergunta::Resposta
```

Esse formato é simples, legível em Markdown e compatível com fluxos comuns de
exportação manual.

## Exportação manual

1. Escolha somente cards úteis e revisados.
2. Copie os cards no formato `Pergunta::Resposta`.
3. Converta para o separador aceito pelo seu fluxo de importação no Anki.
4. Importe em um deck identificado como Bombeiro Comunitário 2026.
5. Revise no Anki sem alterar a fonte principal no Obsidian.

## Cuidados para não duplicar cards

- Exporte em lotes pequenos.
- Mantenha nomes de decks claros.
- Evite exportar cards ainda instáveis.
- Não duplique cards que já existem no Anki.
- Se um card for corrigido no Obsidian, atualize também no Anki ou remova o
  card antigo.

## Fonte oficial

Cards exportados devem continuar obedecendo à hierarquia do projeto:

1. edital;
2. PDFs e apostilas oficiais;
3. manuais oficiais CBMSC;
4. notas atômicas;
5. flashcards e simulados.

Não crie card no Anki com conteúdo fora do edital como se fosse fonte
principal.

## Quando usar Anki

Use Anki para:

- conceitos que precisam de repetição diária;
- pegadinhas recorrentes;
- erros repetidos em simulados;
- números, definições e classificações;
- pontos com baixo domínio apesar de revisão no Obsidian.

## Quando manter apenas Obsidian

Mantenha apenas no Obsidian quando:

- o card ainda precisa ser corrigido;
- o conteúdo depende de contexto longo;
- o tema não é prioridade;
- a nota atômica ainda não foi auditada;
- a exportação criaria duplicação sem ganho real.
