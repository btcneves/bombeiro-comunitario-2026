# Bombeiro Comunitário 2026 — Sistema de Estudo com Obsidian

![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)
![Made with Obsidian](https://img.shields.io/badge/made%20with-Obsidian-7C3AED)
![Markdown](https://img.shields.io/badge/format-Markdown-black)
![Study System](https://img.shields.io/badge/focus-concurso-orange)
![Spaced Repetition](https://img.shields.io/badge/review-spaced%20repetition-1f6feb)

Sistema profissional de estudo para o concurso de Bombeiro Comunitário 2026, estruturado como um second brain em Obsidian. O projeto combina notas atômicas, flashcards, revisão espaçada, dashboard operacional, resumos estratégicos e registro de erros para transformar estudo disperso em um fluxo controlável, auditável e replicável.

## Por que este projeto existe?

Estudar para concurso costuma degradar rápido quando o material fica espalhado entre PDFs, cadernos, apps, prints e resumos improvisados. O resultado é previsível: estudo passivo, revisão irregular, baixa rastreabilidade do edital, acúmulo de assuntos esquecidos e dificuldade para saber o que revisar hoje.

Este projeto resolve esse problema organizando todo o processo em um vault Obsidian com estrutura orientada a execução:

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
└── Obsidian Vault/
```

### O que cada área faz

- `README.md`: visão executiva do projeto e onboarding rápido.
- `docs/`: documentação detalhada da metodologia, arquitetura e operação.
- `assets/`: diretório para diagramas, imagens e materiais visuais de apresentação.
- `.github/`: templates para issues e pull requests.
- `Obsidian Vault/`: núcleo do sistema de estudo, preservado como ambiente operacional.
- `CONTEÚDO PROGRAMÁTICO/` e `Edital/`: materiais-base de referência usados para alimentar o vault.

## Como usar

1. Clone este repositório.
2. Instale o Obsidian no computador ou dispositivo móvel.
3. No Obsidian, selecione `Open folder as vault`.
4. Escolha a pasta `Obsidian Vault`.
5. Abra a nota `🎯 Dashboard`.
6. Revise as pendências do dia.
7. Estude o tópico novo definido no cronograma.
8. Execute os flashcards da disciplina estudada.
9. Registre erros imediatamente após questões ou simulados.

Documentação detalhada:

- [Como usar](docs/como-usar.md)
- [Fluxo de estudo](docs/fluxo-de-estudo.md)
- [Arquitetura](docs/arquitetura.md)
- [Sistema de revisão](docs/sistema-de-revisao.md)

## Fluxo diário recomendado

O ciclo diário sugerido é simples e disciplinado:

1. Abrir o dashboard.
2. Resolver revisões vencidas e atrasadas.
3. Estudar um tópico novo com nota atômica.
4. Responder flashcards do bloco recém-estudado e dos pontos fracos.
5. Registrar erros surgidos em questões ou simulado.
6. Atualizar `nível-domínio`, `última-revisão` e `próxima-revisão`.

Esse fluxo reduz a tendência de “consumir conteúdo” sem consolidar memória de longo prazo.

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
- `v1.1`: inclusão de imagens, fluxos visuais e diagramas operacionais.
- `v1.2`: integração com Anki e exportação de flashcards.
- `v1.3`: simulados automatizados e rotinas de auditoria.
- `v1.4`: apresentação visual do projeto com GitHub Pages.

Roadmap completo em [ROADMAP.md](ROADMAP.md).

## Como contribuir

Contribuições devem preservar a estrutura do vault, manter consistência em Markdown e reforçar a utilidade do sistema como projeto técnico e ambiente de estudo real.

Fluxo recomendado:

1. Abra uma issue explicando o problema, melhoria ou ajuste de conteúdo.
2. Faça alterações pequenas, rastreáveis e bem descritas.
3. Não quebre links, nomes de pastas ou a organização principal do vault.
4. Envie um pull request usando o template do repositório.

Guia completo em [CONTRIBUTING.md](CONTRIBUTING.md).

## Aviso

Este repositório é material de apoio educacional. Ele não substitui a leitura oficial do edital, legislação aplicável, manuais normativos, bibliografia exigida nem instruções da banca organizadora. Em caso de divergência, prevalecem sempre as fontes oficiais.

## Licença

Distribuído sob a licença MIT. Consulte [LICENSE](LICENSE).
