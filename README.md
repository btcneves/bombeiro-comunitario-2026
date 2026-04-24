# Bombeiro Comunitário 2026 — Sistema de Estudo com Obsidian

![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)
![Made with Obsidian](https://img.shields.io/badge/made%20with-Obsidian-7C3AED)
![Markdown](https://img.shields.io/badge/format-Markdown-black)
![Study System](https://img.shields.io/badge/focus-concurso-orange)
![Spaced Repetition](https://img.shields.io/badge/review-spaced%20repetition-1f6feb)

Sistema profissional de estudo para o concurso de Bombeiro Comunitário 2026,
estruturado como um second brain em Obsidian. O projeto combina notas
atômicas, flashcards, revisão espaçada, dashboard operacional, resumos
estratégicos e registro de erros para transformar estudo disperso em um fluxo
controlável, auditável e replicável.

> Aviso institucional: este projeto é independente e não é afiliado,
> mantido, patrocinado ou endossado pela Prefeitura de Imaruí, pelo Instituto
> Fucap ou pelo CBMSC.

## Por que este projeto existe?

Estudar para concurso costuma degradar rápido quando o material fica espalhado
entre PDFs, cadernos, apps, prints e resumos improvisados. O resultado é
previsível: estudo passivo, revisão irregular, baixa rastreabilidade do edital,
acúmulo de assuntos esquecidos e dificuldade para saber o que revisar hoje.

Este projeto resolve esse problema organizando todo o processo em um vault
Obsidian com estrutura orientada a execução:

- centralização do conteúdo em um único sistema
- notas atômicas por conceito, não por apostila inteira
- revisão por ciclo `D+1`, `D+7` e `D+30`
- flashcards integrados ao conteúdo
- registro sistemático de erros
- dashboard central para visão diária de estudo

## Funcionalidades

- Vault Obsidian organizado por edital, disciplinas, tópicos e revisões.
- Notas atômicas com frontmatter padronizado para controle de progresso.
- MOCs e páginas centrais por disciplina.
- Flashcards integrados ao fluxo de estudo.
- Dashboard com consultas Dataview para prioridades e pendências.
- Revisão espaçada com ciclos `D+1`, `D+7` e `D+30`.
- Sistema de erros para revisão direcionada.
- Cronograma e atalhos operacionais dentro do vault.
- Resumos estratégicos para reta final.
- Estrutura adaptável para outros concursos.

## Preview do sistema

O fluxo central do repositório foi desenhado para ser simples de operar no dia
a dia:

`Dashboard → Revisão → Flashcards → Estudo novo → Questões → Erros → Revisão`

Pontos principais de navegação:

- dashboard: [`Obsidian Vault/00 - Dashboard/🎯 Dashboard.md`](<Obsidian Vault/00 - Dashboard/🎯 Dashboard.md>)
- flashcards: [`Obsidian Vault/04 - Flashcards/`](<Obsidian Vault/04 - Flashcards>)
- revisões: [`Obsidian Vault/05 - Revisões/`](<Obsidian Vault/05 - Revisões>)
- erros: [`Obsidian Vault/09 - Erros e Aprendizados/`](<Obsidian Vault/09 - Erros e Aprendizados>)
- edital: [`Edital/`](Edital) e
  [`Obsidian Vault/01 - Edital/`](<Obsidian Vault/01 - Edital>)
- conteúdo programático:
  [`CONTEÚDO PROGRAMÁTICO/`](<CONTEÚDO PROGRAMÁTICO>)

## Estrutura do projeto

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── ROADMAP.md
├── PROJECT_STATUS.md
├── GITHUB_PAGES.md
├── PORTFOLIO.md
├── docs/
├── assets/
├── .github/
├── SOURCES.md
├── NOTICE.md
├── RELEASE_NOTES_v1.0.0.md
└── Obsidian Vault/
```

### O que cada área faz

- `README.md`: visão executiva do projeto e onboarding rápido.
- `docs/`: documentação detalhada da metodologia, arquitetura e operação.
- `assets/`: diretório para diagramas, imagens e materiais visuais de
  apresentação.
- `.github/`: templates para issues e pull requests.
- `SOURCES.md`: documentação das fontes oficiais e materiais públicos usados.
- `NOTICE.md`: aviso de independência institucional e uso educacional.
- `Obsidian Vault/`: núcleo do sistema de estudo, preservado como ambiente
  operacional.
- `CONTEÚDO PROGRAMÁTICO/` e `Edital/`: materiais-base de referência usados
  para alimentar o vault.

## Como usar

1. Clone este repositório.
2. Instale o Obsidian no computador ou dispositivo móvel.
3. No Obsidian, selecione `Open folder as vault`.
4. Escolha a pasta `Obsidian Vault`.
5. Abra a nota `🎯 Dashboard` para entrar pelo centro operacional.
6. Use `05 - Revisões` para limpar revisões vencidas e atrasadas.
7. Estude novos tópicos em `03 - Tópicos Atômicos`.
8. Responda os decks em `04 - Flashcards`.
9. Registre falhas em `09 - Erros e Aprendizados`.
10. Consulte `01 - Edital`, `Edital/` e `CONTEÚDO PROGRAMÁTICO/` para
    rastrear a fonte e a cobertura do conteúdo.

Documentação detalhada:

- [Landing page da documentação](docs/index.md)
- [Como usar](docs/como-usar.md)
- [Fluxo de estudo](docs/fluxo-de-estudo.md)
- [Arquitetura](docs/arquitetura.md)
- [Sistema de revisão](docs/sistema-de-revisao.md)
- [Publicação no GitHub](docs/publicacao-github.md)

## Fluxo diário recomendado

O ciclo diário sugerido é simples e disciplinado:

1. Abrir o dashboard.
2. Resolver revisões vencidas e atrasadas.
3. Estudar um tópico novo com nota atômica.
4. Responder flashcards do bloco recém-estudado e dos pontos fracos.
5. Registrar erros surgidos em questões ou simulado.
6. Atualizar `nível-domínio`, `última-revisão` e `próxima-revisão`.

Esse fluxo reduz a tendência de “consumir conteúdo” sem consolidar memória de
longo prazo.

## Metodologia

O sistema foi desenhado sobre cinco pilares:

- `Active Recall`: recuperação ativa da informação em vez de releitura passiva.
- `Spaced Repetition`: revisão em janelas crescentes para reduzir esquecimento.
- `Zettelkasten leve`: notas pequenas, linkadas e recuperáveis.
- `Notas atômicas`: uma nota por conceito ou bloco cognitivo controlável.
- `Aprendizado por erro`: cada falha relevante gera reforço explícito.

Leitura aprofundada:

- [Metodologia](docs/metodologia.md)
- [Estratégia de aprovação](docs/estrategia-aprovacao.md)
- [Flashcards](docs/flashcards.md)
- [Sistema de erros](docs/sistema-de-erros.md)

## Fontes oficiais

As referências oficiais e os materiais públicos usados neste repositório estão
documentados em [SOURCES.md](SOURCES.md).

Destaques:

- Edital do Concurso Público `001/2026` do Município de Imaruí/SC
- Biblioteca pública de Manuais CBMSC:
  <https://www.cbm.sc.gov.br/index.php/biblioteca/manuais-cbmsc>
- Código de Trânsito Brasileiro, quando aplicável
- Manuais Brasileiros de Sinalização de Trânsito, quando aplicável

Consulte também:

- [SOURCES.md](SOURCES.md)
- [NOTICE.md](NOTICE.md)
- [docs/index.md](docs/index.md)
- [docs/publicacao-github.md](docs/publicacao-github.md)

Em caso de divergência, prevalecem sempre as fontes oficiais.

## Tecnologias e ferramentas

- Obsidian
- Markdown
- Dataview
- Spaced Repetition
- Templater
- Git
- GitHub
- GitHub Pages

## Roadmap

- `v1.0`: vault consolidado e documentação profissional do repositório.
- `v1.0.1`: publicação e acabamento GitHub.
- `v1.1`: inclusão de imagens, fluxos visuais e diagramas operacionais.
- `v1.2`: integração com Anki e exportação de flashcards.
- `v1.3`: simulados automatizados e rotinas de auditoria.
- `v1.4`: apresentação visual do projeto com GitHub Pages.

Roadmap completo em [ROADMAP.md](ROADMAP.md).

## Como contribuir

Contribuições devem preservar a estrutura do vault, manter consistência em
Markdown e reforçar a utilidade do sistema como projeto técnico e ambiente de
estudo real.

Fluxo recomendado:

1. Abra uma issue explicando o problema, melhoria ou ajuste de conteúdo.
2. Faça alterações pequenas, rastreáveis e bem descritas.
3. Não quebre links, nomes de pastas ou a organização principal do vault.
4. Envie um pull request usando o template do repositório.

Guia completo em [CONTRIBUTING.md](CONTRIBUTING.md).

## Metadados recomendados no GitHub

Description:

`Sistema de estudo com Obsidian para Bombeiro Comunitário 2026, com notas
atômicas, flashcards, revisão espaçada e dashboard.`

Topics sugeridos:

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

## Aviso

Este repositório é material de apoio educacional. Ele não substitui a leitura
oficial do edital, legislação aplicável, manuais normativos, bibliografia
exigida nem instruções da banca organizadora.

Consulte [NOTICE.md](NOTICE.md) para o aviso institucional completo.

Em caso de divergência, prevalecem sempre as fontes oficiais.

## Licença

Distribuído sob a licença MIT. Consulte [LICENSE](LICENSE).
