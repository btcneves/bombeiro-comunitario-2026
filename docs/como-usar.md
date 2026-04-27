# Como usar

## Instalação e abertura do vault

1. Instale o Obsidian no seu computador ou celular.
2. Clone este repositório ou baixe o conteúdo como arquivo compactado.
3. Abra o Obsidian.
4. Clique em `Open folder as vault`.
5. Selecione a pasta `Obsidian Vault`.
6. Aguarde o carregamento inicial do vault.
7. Abra a nota `🎯 Dashboard`.

## Plugins recomendados

O vault já foi pensado para funcionar melhor com estes plugins:

- `Dataview`
- `Spaced Repetition`
- `Calendar` opcional
- `Templater` opcional

Pelo estado atual do vault, os plugins também configurados localmente incluem
`Excalidraw` e `Tasks`, mas os dois citados como opcionais acima não são
obrigatórios para começar a usar o sistema.

## Como ativar plugins

1. No Obsidian, abra `Settings`.
2. Entre em `Community plugins`.
3. Ative community plugins se ainda estiverem desabilitados.
4. Procure e instale:
   - `Dataview`
   - `Spaced Repetition`
   - `Calendar`
   - `Templater`
5. Habilite os plugins instalados.

## Primeiro uso

Após abrir o vault:

1. vá para `🎯 Dashboard`
2. observe revisões do dia e atrasadas
3. entre na disciplina do bloco que será estudado
4. abra a nota atômica correspondente
5. revise o conteúdo
6. responda os flashcards da área
7. registre erros no diretório `09 - Erros e Aprendizados`
8. atualize datas e domínio da nota revisada

## Fluxo mínimo de trabalho

- Use o dashboard como entrada principal.
- Use `03 - Tópicos Atômicos` como núcleo do conhecimento.
- Use `04 - Flashcards` para recuperação ativa.
- Use `05 - Revisões` para controlar o ciclo.
- Use `09 - Erros e Aprendizados` para reforço dirigido.

## Guia completo

Para rotinas detalhadas por tempo disponível, hierarquia de fonte, checklist
diário e orientações específicas sobre CBAE, consulte:

[**docs/guia-de-estudo-eficiente.md**](guia-de-estudo-eficiente.md)

---

## Solução de problemas

### Notas não aparecem

Verifique se você abriu a pasta correta. O vault deve ser a pasta
`Obsidian Vault`, não a raiz do repositório.

### Dataview não renderiza

Confirme que o plugin `Dataview` está instalado e habilitado. Sem ele, as
tabelas do dashboard e dos índices aparecerão como blocos de código.

### Flashcards não aparecem

Confirme que o plugin `Spaced Repetition` está ativo e que os cards estão no
formato esperado, como `Pergunta::Resposta` ou no padrão aceito pelo plugin
usado no vault.

### Caracteres especiais em nomes de pastas

Este projeto usa nomes em português com espaços e acentos. Em sistemas que
extraem ZIP incorretamente ou ferramentas que alteram codificação, prefira
clonar com Git para preservar os nomes dos diretórios.

### Links do Obsidian não funcionam

Isso normalmente indica que o vault foi aberto de forma parcial ou fora da
pasta correta. Reabra especificamente `Obsidian Vault`.
