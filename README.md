# Bombeiro Comunitário 2026 — Sistema de Estudo com Obsidian

[GitHub Pages](https://btcneves.github.io/bombeiro-comunitario-2026/) ·
[Documentação](docs/index.md) · [Fontes oficiais](SOURCES.md) ·
[Notice](NOTICE.md)

![Status](https://img.shields.io/badge/status-active-success)
![Release](https://img.shields.io/badge/release-v1.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Made with Obsidian](https://img.shields.io/badge/made%20with-Obsidian-7C3AED)
![Markdown](https://img.shields.io/badge/format-Markdown-black)

Sistema profissional de estudo para o concurso de Bombeiro Comunitário 2026,
estruturado como um second brain em Obsidian. O projeto combina notas
atômicas, flashcards, revisão espaçada, simulados, matriz de desempenho,
registro de erros, auditoria de fontes e documentação pública.

> Aviso institucional: este projeto é autônomo e não é afiliado,
> mantido, patrocinado ou endossado pela Prefeitura de Imaruí, pelo Instituto
> Fucap ou pelo CBMSC.

## Como usar

1. Clone este repositório.
2. Abra o Obsidian.
3. Selecione `Open folder as vault`.
4. Escolha a pasta `Obsidian Vault`.
5. Abra `🎯 Dashboard` para iniciar pelo centro operacional.
6. Revise pendências, faça flashcards, estude tópicos, resolva questões e
   registre erros.

Atalhos principais:

- 🎯 Dashboard: [`Obsidian Vault/00 - Dashboard/🎯 Dashboard.md`](<Obsidian Vault/00 - Dashboard/🎯 Dashboard.md>)
- Flashcards: [`Obsidian Vault/04 - Flashcards/`](<Obsidian Vault/04 - Flashcards>)
- Questões e simulados: [`Obsidian Vault/06 - Questões/`](<Obsidian Vault/06 - Questões>)
- Erros: [`Obsidian Vault/09 - Erros e Aprendizados/`](<Obsidian Vault/09 - Erros e Aprendizados>)
- Edital e fontes: [`Edital/`](Edital), [`CONTEÚDO PROGRAMÁTICO/`](<CONTEÚDO PROGRAMÁTICO>) e [SOURCES.md](SOURCES.md)

## Fidelidade ao edital

O projeto segue uma hierarquia rígida de fontes:

1. edital;
2. PDFs e apostilas oficiais;
3. manuais oficiais CBMSC;
4. notas atômicas;
5. flashcards e simulados;
6. observações complementares.

Em caso de divergência, prevalecem as fontes oficiais. No CBAE, a
nomenclatura principal é "Avaliação da Cena" e "Avaliação Geral da Vítima",
conforme auditoria do Manual CBAE.

## Documentação

- [Landing page da documentação](docs/index.md)
- [Como usar](docs/como-usar.md)
- [Guia de estudo eficiente](docs/guia-de-estudo-eficiente.md)
- [Fluxo de estudo](docs/fluxo-de-estudo.md)
- [Arquitetura](docs/arquitetura.md)
- [Metodologia](docs/metodologia.md)
- [Sistema de revisão](docs/sistema-de-revisao.md)
- [Sistema de erros](docs/sistema-de-erros.md)

## Simulados

O vault inclui 3 simulados autorais e 100 questões no estilo provável da banca
Instituto Fucap, com 5 alternativas e uma correta.

- [Simulados estilo Instituto Fucap](docs/simulados-fucap.md)
- [Simulados avançados](docs/simulados-avancados.md)
- [Banco de questões](<Obsidian Vault/06 - Questões/_Banco de Questões.md>)
- [Plano de simulados](<Obsidian Vault/06 - Questões/Plano de Simulados.md>)
- [Checklist pós-simulado](<Obsidian Vault/06 - Questões/Checklist Pós-Simulado.md>)
- [Matriz de desempenho](<Obsidian Vault/06 - Questões/Matriz de Desempenho.md>)

## Flashcards e Anki

Os flashcards usam o padrão `Pergunta::Resposta` e ficam próximos das notas e
fontes oficiais. O Obsidian permanece como fonte principal, e o Anki pode ser
usado para repetição intensiva de cards selecionados.

- [Flashcards](docs/flashcards.md)
- [Integração com Anki](docs/integracao-anki.md)
- [Decks no vault](<Obsidian Vault/04 - Flashcards>)

## Qualidade do banco de questões

Os simulados passam por auditoria automatizada para garantir que o gabarito não seja previsível por chute posicional ou por padrões linguísticos das alternativas.

```bash
python3 scripts/auditoria_gabaritos.py --audit
# Exit 0 = sem violações. Exit 1 = há problemas.
```

Última auditoria (2026-04-29): A=B=C=D=E=**20%** — distribuição uniforme. Ver [`AGENTS.md`](AGENTS.md) para regras obrigatórias ao criar questões.

## Auditorias

- [Auditoria do edital](docs/auditoria-edital.md)
- [Auditoria Português](docs/auditoria-portugues.md)
- [Auditoria Trânsito](docs/auditoria-transito.md)
- [Auditoria CIE](docs/auditoria-cie.md)
- [Auditoria CBAE](docs/auditoria-cbae.md)
- [Auditoria IG 10-03-BM](docs/auditoria-ig-10-03-bm.md)
- [Auditoria educacional CBAE](docs/auditoria-protocolo-aph.md)
- [**Auditoria de Gabaritos**](docs/relatorios/) — 2026-04-29, A=B=C=D=E=20%

## Diagramas

- [Arquitetura do vault](assets/diagramas/arquitetura-do-vault.md)
- [Fluxo de estudo completo](assets/diagramas/fluxo-de-estudo-completo.md)
- [Ciclo de melhoria](assets/diagramas/ciclo-de-melhoria.md)
- [Fidelidade ao edital](assets/diagramas/fidelidade-ao-edital.md)
- [Imagens futuras](assets/imagens/README.md)

## Adaptação para outros concursos

A metodologia pode ser replicada, mas este repositório permanece específico
para Bombeiro Comunitário 2026.

- [Adaptando para outros concursos](docs/adaptando-para-outros-concursos.md)
- [Checklist para novo concurso](docs/checklist-novo-concurso.md)

## Release atual

- `v1.0.0`: vault e documentação inicial.
- `v1.0.1`: auditorias, guia de estudo e simulados estilo FUCAP.
- `v1.1.0`: consolidação do roadmap atual com diagramas, Anki documentado,
  simulados avançados, GitHub Pages e adaptabilidade.

## Roadmap

O roadmap atual está consolidado em [ROADMAP.md](ROADMAP.md). Itens futuros
incluem screenshots reais, automação de exportação Anki, geração programática
de simulados, validação automática de links e CI simples para Markdown.

## Fontes oficiais

As referências oficiais e os materiais públicos usados estão documentados em
[SOURCES.md](SOURCES.md).

Consulte também:

- [NOTICE.md](NOTICE.md)
- [GITHUB_PAGES.md](GITHUB_PAGES.md)
- [Publicação no GitHub](docs/publicacao-github.md)

## Licença

Distribuído sob a licença MIT. Consulte [LICENSE](LICENSE).
