# Adaptando para outros concursos

Este projeto foi desenhado para Bombeiro Comunitário 2026, mas a arquitetura
pode ser reutilizada em outros editais. A regra é adaptar o conteúdo sem
destruir o sistema.

## Checklist de adaptação

Use o checklist prático em [Checklist para novo concurso](checklist-novo-concurso.md)
como roteiro operacional.

## Trocar edital

Substitua ou adicione o novo edital em uma pasta de referência clara. Depois,
atualize as notas de `01 - Edital` com:

- cargo;
- banca;
- cronograma;
- conteúdo programático;
- critérios de prova;
- peso das disciplinas.

O edital continua sendo a fonte primária de escopo.

## Auditar fontes

Antes de criar notas, identifique fontes oficiais:

- edital;
- apostilas indicadas;
- legislação;
- manuais oficiais;
- documentos públicos da banca.

Registre tudo em `SOURCES.md` e atualize `NOTICE.md` quando o contexto
institucional mudar.

## Criar MOCs

Em `02 - Disciplinas`, crie páginas centrais por disciplina. Cada MOC deve
apontar para tópicos atômicos, flashcards, resumos e questões relevantes.

## Criar notas atômicas

Em `03 - Tópicos Atômicos`, crie uma nota por conceito ou subtópico do edital.
Preserve frontmatter e controle de revisão.

## Adaptar simulados

Simulados devem refletir o novo edital:

- número de questões;
- alternativas;
- distribuição por disciplina;
- estilo provável da banca;
- fonte e nota relacionada;
- uma única resposta correta.

Não reaproveite questão de Bombeiro Comunitário como se fosse conteúdo de
outro concurso sem auditar escopo e fonte.

## Preservar metodologia

Mantenha:

- dashboard;
- notas atômicas;
- flashcards;
- revisão espaçada;
- sistema de erros;
- matriz de desempenho;
- documentação pública.

## Revisar documentos legais e públicos

Antes de publicar uma adaptação:

- revise `LICENSE`;
- revise `SOURCES.md`;
- revise `NOTICE.md`;
- atualize README;
- atualize release notes;
- confira se nomes de órgãos, banca e concurso estão corretos.

## Criar nova release

Quando a adaptação estiver validada:

1. rode validação de links;
2. confira arquivos obrigatórios;
3. confirme que fontes oficiais foram preservadas;
4. atualize `CHANGELOG.md`;
5. crie release notes;
6. crie tag específica para o novo concurso.
