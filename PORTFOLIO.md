# Portfólio Técnico

**Bombeiro Comunitário 2026 — Sistema de Estudo com Obsidian**

Sistema documental e operacional de estudo para concurso público, estruturado
como um second brain em Obsidian e versionado como repositório GitHub
profissional.

## Problema

Preparação para concurso costuma degradar quando o conteúdo fica espalhado, a
revisão é inconsistente e o estudante perde a conexão entre edital, estudo,
questões, erro e retomada.

## Solução

O projeto centraliza estudo, revisão, flashcards, cronograma, documentação e
controle de erros em uma arquitetura única. Em vez de depender de PDFs,
resumos e marcações soltas, o estudante opera um fluxo rastreável dentro de um
vault Obsidian versionado no GitHub.

## Tecnologias usadas

- Obsidian
- Markdown
- Dataview
- Spaced Repetition
- Git
- GitHub
- GitHub Pages

## Decisões técnicas

- uso de Markdown como formato principal para longevidade e portabilidade
- frontmatter estruturado para rastrear revisão, domínio e prioridade
- documentação externa ao vault para apresentação pública e manutenção
- separação entre conteúdo operacional, documentação e materiais de referência
- versionamento com Git para histórico, auditoria e publicação

## Decisões de arquitetura

- separação por camadas: dashboard, edital, disciplinas, notas atômicas,
  flashcards, revisões, questões, resumos e erros
- notas atômicas para granularidade cognitiva e reutilização
- flashcards no próprio ambiente de estudo para reduzir fricção operacional
- sistema de erros como mecanismo de realimentação
- documentação externa ao vault para transformar o sistema em produto técnico
  apresentável

## Metodologia de aprendizado

- active recall para medir recuperação em vez de releitura
- spaced repetition com ciclos `D+1`, `D+7` e `D+30`
- notas atômicas para reduzir ambiguidade e facilitar revisão
- ligação entre erro, nota, card e revisão para reforço dirigido

## Impacto prático

- maior clareza sobre o que estudar e o que revisar
- redução de estudo passivo
- melhor retenção por revisão espaçada
- correção sistemática de erros recorrentes
- transformação de um vault pessoal em ativo técnico publicável

## Habilidades demonstradas

- organização de conhecimento
- documentação técnica
- Markdown
- Git/GitHub
- Obsidian
- arquitetura de informação
- pensamento sistêmico
- automação de estudo
- versionamento
- modelagem de informação em Markdown

## Como apresentar esse projeto em entrevista ou portfólio

Uma narrativa objetiva para apresentação:

1. descrever o problema de estudo fragmentado e revisão inconsistente
2. explicar que a solução foi projetar um sistema de conhecimento em Obsidian
3. mostrar a arquitetura em camadas e o fluxo diário de uso
4. destacar decisões de documentação, versionamento e publicação
5. concluir com o valor prático: organização, retenção, rastreabilidade e
   transformação de necessidade real em produto técnico publicável
