# Guia de Estudo Eficiente

Sistema profissional de estudo com Obsidian para Bombeiro Comunitário 2026.
Este guia explica como extrair o máximo do repositório com o menor desperdício
de tempo e energia.

---

## Objetivo

Este repositório não é uma coleção de arquivos de texto. É uma **plataforma de
estudo ativa** composta por:

- edital e apostilas oficiais como fonte de verdade
- notas atômicas alinhadas a essas fontes
- flashcards integrados para recuperação ativa
- revisão espaçada para evitar esquecimento
- sistema de erros para transformar falhas em reforço
- dashboard operacional para controle diário

O objetivo não é acumular notas. É **reter conteúdo certo, de fonte certa, no
tempo certo**.

---

## Regra principal — hierarquia de fonte

Antes de qualquer coisa, grave esta ordem:

1. **Edital** — define o que cai e o que não cai
2. **Apostilas e PDFs oficiais do edital** — definem o que a banca espera
3. **Manuais oficiais CBMSC** — definem a nomenclatura e os procedimentos
4. **Notas atômicas do vault** — organizam o estudo dessas fontes
5. **Flashcards** — testam o que as notas ensinam
6. **Questões** — diagnosticam o nível real de domínio
7. **Registro de erros** — corrigem e reforçam pontos fracos

Se houver conflito entre qualquer fonte e o edital ou apostila oficial: **a
apostila oficial prevalece sempre**.

> Exemplo aplicado ao CBAE: o Manual CBAE usa "Avaliação Geral da Vítima" como
> nomenclatura oficial, não "ABCDE". Para fins de prova, a resposta correta
> segue o manual — não o mnemônico externo.

---

## Rotina diária recomendada

Execute nesta ordem. Não inverta as etapas.

1. **Abrir o Dashboard** — `Obsidian Vault/00 - Dashboard/🎯 Dashboard.md`
2. **Ver revisões vencidas** — toda revisão atrasada tem prioridade sobre
   conteúdo novo
3. **Revisar notas com `próxima-revisão` no dia** — releitura rápida com foco
   em recuperação, não em anotação
4. **Fazer flashcards do dia** — pelo plugin Spaced Repetition ou revisão
   manual dos decks
5. **Estudar um tópico novo de alta prioridade** — uma nota atômica completa,
   finalizada, linkada
6. **Resolver questões ou simular perguntas** — ao menos 5-10 questões do tema
   estudado
7. **Registrar erros** — todo erro com causa e ação de correção
8. **Atualizar metadados da nota** — `nível-domínio`, `última-revisão`,
   `próxima-revisão`

---

## Como usar o Obsidian Vault

| Pasta | Função |
|---|---|
| `00 - Dashboard` | Centro de comando diário. Revisões, agenda, cronograma. |
| `01 - Edital` | Escopo oficial. O que cai e como está organizado. |
| `02 - Disciplinas` | Mapa por matéria. Visão macro de cada área. |
| `03 - Tópicos Atômicos` | Conteúdo principal. Uma nota por conceito. |
| `04 - Flashcards` | Decks por disciplina. Recuperação ativa diária. |
| `05 - Revisões` | Controle de revisão espaçada. |
| `06 - Questões` | Banco de questões e simulados. |
| `08 - Resumos Estratégicos` | Revisão rápida para reta final. |
| `09 - Erros e Aprendizados` | Registro e correção de falhas. |

---

## Método de máxima eficiência

- **Não comece por leitura passiva.** Ler o PDF sem fazer nota atômica não
  consolida. Leia com a nota aberta.
- **Revisar antes de estudar novo.** Revisão vencida tem prioridade.
- **Flashcard é teste, não leitura.** Tente responder antes de ver a resposta.
- **Todo erro importante vai para o sistema de erros.** Erro sem registro vira
  erro repetido.
- **Priorize pontos fracos, não assuntos fáceis.** O que você já sabe não
  precisa de mais tempo.
- **A fonte oficial é critério final.** Não substitua apostila por mnemônico
  externo.
- **Cada erro vira uma ação.** Registrar o erro, identificar a causa, rever a
  nota, reforçar o card.

---

## Ciclo ideal de estudo

```
Dashboard → Revisão vencida → Flashcards → Estudo novo
→ Questões → Registro de erros → Atualização de domínio → Próxima revisão
```

Não pule etapas quando tiver tempo. Quando o tempo estiver curto, priorize
revisão e flashcards antes de estudo novo.

---

## Como estudar CBAE corretamente

CBAE é a disciplina de maior peso técnico no concurso. Erros de nomenclatura
custam pontos.

### Nomenclatura oficial — Manual CBAE

O Manual CBAE CBMSC **não usa ABCDE nem XABCDE** como estrutura central. A
nomenclatura oficial é:

**Avaliação da Cena** + **Avaliação Geral da Vítima**

Sequência oficial (Manual CBAE, p. 98):
1. Impressão geral — trauma (lesão por fator externo) ou emergência médica /
   intercorrência clínica (doença por fator intrínseco)
2. Nível de consciência
3. Permeabilidade das vias aéreas + coluna cervical
4. Respiração
5. Hemorragias graves

### Distinção trauma × clínico

O manual diferencia explicitamente (p. 108):

| Situação | Manobra de vias aéreas |
|---|---|
| Caso clínico (sem trauma) | Extensão de cabeça |
| Trauma | Empurre mandibular (assumir cervical em todo trauma) |

### Sobre torniquete

O Manual CBAE afirma que torniquete é **técnica avançada** e não a aborda como
conduta básica (p. 118). A resposta esperada para controle de hemorragia básica
é pressão direta e curativo compressivo.

### Onde aprofundar

- `docs/auditoria-protocolo-aph.md` — relatório completo da auditoria
- `Obsidian Vault/08 - Resumos Estratégicos/Avaliação Geral da Vítima vs ABCDE e XABCDE.md` — nota estratégica com trechos literais do manual

---

## Como medir domínio

O frontmatter de cada nota atômica tem o campo `nível-domínio`. Use:

| Nível | Significado |
|---|---|
| `0` | Não estudado ainda |
| `1` | Visto uma vez |
| `2` | Revisado, entendido mas não testado |
| `3` | Dominado — acertei flashcards, questões e consigo explicar sem consultar |

**Não marque 3 sem:**
- ter respondido os flashcards da nota sem errar
- ter acertado questões sobre o tema
- conseguir explicar o conteúdo em voz alta sem consultar
- não ter repetido o erro na última revisão

---

## Rotinas por tempo disponível

### 30 minutos

| Bloco | Tempo |
|---|---|
| Revisão vencida | 10 min |
| Flashcards | 10 min |
| Erro ou tópico crítico | 10 min |

### 1 hora

| Bloco | Tempo |
|---|---|
| Revisão | 15 min |
| Flashcards | 15 min |
| Estudo novo | 20 min |
| Erros ou questões | 10 min |

### 2 horas

| Bloco | Tempo |
|---|---|
| Revisão | 30 min |
| Flashcards | 20 min |
| Estudo novo | 45 min |
| Questões e erros | 25 min |

### 3 horas

| Bloco | Tempo |
|---|---|
| Revisão | 45 min |
| Flashcards | 30 min |
| Estudo novo | 60 min |
| Questões | 30 min |
| Atualização do sistema | 15 min |

---

## Erros comuns

- Ler o PDF sem transformar em nota atômica — a leitura evaporou.
- Avançar conteúdo novo com revisão vencida acumulada — a pilha cresce.
- Não registrar erros — os mesmos erros se repetem na prova.
- Estudar assunto fora do edital — tempo perdido.
- Decorar mnemônico externo sem verificar na apostila oficial — risco de
  resposta errada se a banca seguir o manual.
- Acumular notas sem fazer flashcards — o conteúdo não entra na memória.
- Marcar domínio como 3 sem testar de verdade — falsa segurança.

---

## Checklist diário

Copie e use diariamente, ou crie uma nota de revisão diária com este modelo:

```markdown
- [ ] Abri o dashboard.
- [ ] Verifiquei revisões vencidas.
- [ ] Fiz flashcards do dia.
- [ ] Estudei tópico prioritário.
- [ ] Resolvi questões.
- [ ] Registrei erros.
- [ ] Atualizei próxima revisão e domínio.
- [ ] O conteúdo estudado está alinhado à fonte oficial.
```

---

## Fontes de referência complementar

- [README.md](../README.md) — visão geral do projeto
- [docs/metodologia.md](metodologia.md) — base metodológica do sistema
- [docs/fluxo-de-estudo.md](fluxo-de-estudo.md) — rotina detalhada
- [docs/sistema-de-erros.md](sistema-de-erros.md) — como usar o sistema de erros
- [docs/flashcards.md](flashcards.md) — como usar os decks de flashcards
- [docs/auditoria-protocolo-aph.md](auditoria-protocolo-aph.md) — auditoria CBAE
- [SOURCES.md](../SOURCES.md) — fontes oficiais do projeto
