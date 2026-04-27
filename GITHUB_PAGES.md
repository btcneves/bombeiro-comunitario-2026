# GitHub Pages

Este repositório foi preparado para ser publicado também como página pública de
apresentação do projeto.

## Objetivo da publicação

Usar o GitHub Pages para transformar a documentação em uma vitrine técnica do
sistema de estudo, útil tanto para leitores quanto para apresentação de
portfólio.

## Caminho recomendado — `main` + `/docs`

1. Faça push da branch `main`.
2. No GitHub, abra `Settings`.
3. Entre em `Pages`.
4. Em `Build and deployment`, escolha `Deploy from a branch`.
5. Selecione a branch `main`.
6. Escolha a pasta `/docs`.
7. Salve.
8. Aguarde a publicação.
9. Copie a URL gerada e adicione esse link no campo `Website` do repositório.

## Caminho alternativo — `main` + `/(root)`

1. Faça push da branch `main`.
2. No GitHub, abra `Settings`.
3. Entre em `Pages`.
4. Em `Build and deployment`, escolha `Deploy from a branch`.
5. Selecione a branch `main`.
6. Escolha a pasta `/(root)`.
7. Salve.

## Estrutura já preparada

Para facilitar a publicação:

- o `README.md` apresenta o projeto de forma executiva
- a pasta `docs/` concentra documentação navegável
- `docs/index.md` funciona como landing page do Pages
- `docs/_config.yml` define título, descrição e tema Jekyll
- `docs/publicacao-github.md` reúne orientações de metadados e release
- `assets/` está pronta para receber imagens e diagramas públicos

## Recomendação prática

Para uma apresentação mais limpa, prefira publicar a partir de `/docs`, usando
`docs/index.md` como porta de entrada. Isso separa a vitrine pública do
restante da raiz técnica do repositório.

URL inferida para este repositório:

`https://btcneves.github.io/bombeiro-comunitario-2026/`

## Conteúdo sugerido para a página pública

A página publicada deve destacar:

- o problema resolvido
- a metodologia do sistema
- a arquitetura do vault
- o fluxo de estudo diário
- a adaptação para outros concursos
- o valor do projeto como portfólio técnico

## Observação

GitHub Pages serve bem para documentação Markdown. Se no futuro houver
necessidade de layout visual mais rico, o mesmo conteúdo pode ser migrado para
um gerador estático sem perder a estrutura documental já criada.
