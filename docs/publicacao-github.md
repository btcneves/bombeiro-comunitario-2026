# Publicação no GitHub

## Metadados recomendados

Description:

Sistema de estudo com Obsidian para Bombeiro Comunitário 2026, com notas
atômicas, flashcards, revisão espaçada e dashboard.

Topics:

- `obsidian`
- `markdown`
- `study-system`
- `spaced-repetition`
- `flashcards`
- `concurso-publico`
- `bombeiro-comunitario`
- `second-brain`
- `zettelkasten`
- `cbmsc`

## GitHub Pages

Configuração recomendada:

1. Abra o repositório no GitHub.
2. Entre em `Settings`.
3. Acesse `Pages`.
4. Em `Build and deployment`, escolha `Deploy from a branch`.
5. Selecione a branch `main`.
6. Escolha a pasta `/docs`.
7. Salve e aguarde a publicação.
8. Adicione a URL publicada no campo `Website` do repositório.

## Release

Para criar a tag da primeira release pública:

```bash
git tag -a v1.0.0 -m "First public release"
git push origin v1.0.0
```

Depois, crie a release no GitHub usando o conteúdo de
`RELEASE_NOTES_v1.0.0.md` como base para a descrição.
