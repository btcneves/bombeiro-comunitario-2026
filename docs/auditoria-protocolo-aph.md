# Relatório de Auditoria — Protocolo APH (Avaliação Geral da Vítima, ABCDE e XABCDE)

**Data:** 2026-04-27
**Executor:** Claude Code (auditoria solicitada pelo autor do projeto)
**Projeto:** bombeiro-comunitario-2026

---

## Objetivo

Auditar, validar e corrigir todo o conteúdo do vault Obsidian relacionado à avaliação de vítimas em emergência, especialmente a diferença entre atendimento ao trauma e atendimento clínico, garantindo alinhamento com o edital do concurso e os PDFs/apostilas oficiais.

---

## Fontes consultadas

| Fonte | Tipo | Localização no projeto |
|---|---|---|
| `MANUAL_CBAE.pdf` | PDF oficial CBMSC — fonte primária | `CONTEÚDO PROGRAMÁTICO/CONHECIMENTOS ESPECÍFICOS/` |
| `EDITAL DE CONCURSO PUBLICO.pdf` | Edital oficial concurso 001/2026 Imaruí/SC | `Edital/` |
| `IG 10-03-BM.pdf` | Instrução Geral CBMSC | `CONTEÚDO PROGRAMÁTICO/CONHECIMENTOS ESPECÍFICOS/` |
| `MANUAL_CIE.pdf` | Manual de Combate a Incêndios | `CONTEÚDO PROGRAMÁTICO/CONHECIMENTOS ESPECÍFICOS/` |
| Biblioteca CBMSC online | Página pública de manuais | https://www.cbm.sc.gov.br/index.php/biblioteca/manuais-cbmsc |

**Ferramenta de extração:** `pdftotext` (Poppler 24.02.0) — instalado em `/usr/bin/pdftotext`.

---

## Termos pesquisados e resultados

### Nos PDFs oficiais

| Termo | MANUAL_CBAE.pdf | IG 10-03-BM.pdf | MANUAL_CIE.pdf | EDITAL |
|---|---|---|---|---|
| `ABCDE` | **Zero ocorrências** | Zero | Zero | Zero |
| `XABCDE` / `X-ABCDE` | **Zero ocorrências** | Zero | Zero | Zero |
| `avaliação geral da vítima` | **Sim — Lição IV, pp. 97-98** | Só como item curricular | Não | Não |
| `avaliação da cena` | **Sim — p. 97** | Só como item curricular | Não | Não |
| `trauma` / `intercorrência clínica` | **Sim — definições p. 98-99** | Sim (contextual) | Sim (contextual) | Não |
| `hemorragia` | **Sim — pp. 116-120** | Só como item curricular | Não relevante | Não |
| `vias aéreas` | **Sim — pp. 105-115** | Só como item curricular | Não relevante | Não |
| `torniquete` | **Sim — p. 118** (definido como técnica avançada, fora de escopo do CBAE) | Não | Não | Não |
| `primeiros socorros` | Sim — todo o capítulo Lição IV | Sim | Não | Sim |

### No vault Obsidian (arquivos .md)

| Termo | Ocorrências | Classificação |
|---|---|---|
| `XABCDE` / `X-ABCDE` | **Zero** | — |
| `ABCDE` | 12+ ocorrências em 8 arquivos | Incorreto como eixo principal |
| `Avaliação Geral da Vítima` | Zero | Lacuna crítica |
| `trauma` / `traumático` | Múltiplas ocorrências | Contextualmente adequado |
| `torniquete` | 4 ocorrências em 3 arquivos | Ensinado como conduta básica — divergência com o manual |
| `ABCDE do trauma` | 1 ocorrência (Primeiros Socorros no Trânsito.md:35) | Rótulo incorreto |

---

## Evidências literais do Manual CBAE

### Avaliação Geral da Vítima — p. 98

> "Para realizar a avaliação, siga os seguintes passos:
> - forme uma impressão geral da vítima, tentando verificar se a pessoa sofreu um **trauma** ou **emergência médica** (doenças em geral);
> - avalie o **nível de consciência** da vítima (se está consciente ou não);
> - avalie a **permeabilidade das vias aéreas** (ou seja, a existência de passagem de ar pelo nariz e/ou boca) **bem como a coluna cervical** (presença de deformidade);
> - observe a **respiração** da vítima verificando se há movimentos respiratórios (normalmente, ocorre a elevação do tórax e abdômen);
> - verifique a presença de **hemorragias graves** (aquelas que possam fazer a vítima perder muito sangue e comprometer a vida);"

### Glossário — p. 98

> "**Intercorrência clínica:** Também denominada Emergência médica, é causada por fatores intrínsecos, ou seja, por disfunção do organismo. Não existe um fator externo atuando para provocar a lesão. São exemplos doenças que alteram os parâmetros normais de uma pessoa (dificuldade de respirar, fraqueza, formigamento), tais como: diabetes, tumores e doenças cardíacas."

### Manobras de abertura de VA — p. 108 (quadro literal)

> "Em caso clínico = manobra de extensão de cabeça"
> "Em caso de trauma = manobra de empurre mandibular"
>
> "Ao realizar qualquer procedimento de abertura de vias aéreas, você deve estar atento/ciente a:
> 1. assumir lesões associadas de cervical em todos os casos de trauma;
> 2. evitar a hiperextensão do pescoço ou qualquer movimento da cabeça e pescoço com a finalidade de prevenir maior dano à coluna vertebral."

### Torniquete — p. 118

> "A resposta é bastante simples: o uso do torniquete não será abordado neste material por ser considerada uma técnica avançada, devendo ser realizada após a orientação de um socorrista treinado."

---

## Decisão metodológica adotada

1. **Eixo principal do vault:** "Avaliação Geral da Vítima" (nomenclatura literal do Manual CBAE).
2. **ABCDE:** mantido apenas como "Observação complementar" em bloco separado, com indicação de que não é a nomenclatura do manual oficial.
3. **XABCDE:** não introduzido. Sem respaldo em nenhuma fonte oficial do projeto.
4. **Torniquete:** mantido nas notas (informação útil como conhecimento periférico), mas marcado explicitamente como "técnica avançada — não cobrada como conduta principal pelo Manual CBAE".
5. **Distinção trauma × clínico:** baseada exclusivamente na distinção do manual — glossário (p. 98) + manobras de VA (p. 108).

---

## Arquivos alterados

| Arquivo | Tipo de alteração |
|---|---|
| `03 - Tópicos Atômicos/CBAE/CBAE - Avaliação da Cena e Segurança.md` | Reescrita — eixo "Avaliação Geral da Vítima"; ABCDE movido para bloco complementar |
| `03 - Tópicos Atômicos/CBAE/CBAE - Lição IV - Noções de Primeiros Socorros.md` | Seção "Avaliação da Vítima — ABCDE" reescrita para nomenclatura CBAE |
| `03 - Tópicos Atômicos/CBAE/CBAE - Hemorragia e Estado de Choque.md` | Torniquete marcado como técnica avançada; cards atualizados |
| `03 - Tópicos Atômicos/CBAE/CBAE - Vias Aéreas e Ventilação.md` | Distinção trauma×clínico formalizada (extensão cabeça vs empurre mandibular) |
| `03 - Tópicos Atômicos/CBAE/CBAE - Intoxicação e Envenenamento.md` | "ABCDE" substituído por "sequência de avaliação do manual" |
| `03 - Tópicos Atômicos/Trânsito/Primeiros Socorros no Trânsito.md` | "ABCDE do trauma" removido como rótulo; sequência CBAE adotada |
| `04 - Flashcards/Deck Emergências.md` | Bloco "Avaliação Inicial — ABCDE" reescrito; cards novos adicionados |
| `04 - Flashcards/Deck Trânsito.md` | Card de "Protocolo ABCDE" atualizado |
| `08 - Resumos Estratégicos/Pegadinhas Fucap.md` | Item CBAE sobre ABCDE atualizado |
| `09 - Erros e Aprendizados/Erros - CBAE.md` | Referência a ABCDE atualizada |

## Arquivos criados

| Arquivo | Finalidade |
|---|---|
| `08 - Resumos Estratégicos/Avaliação Geral da Vítima vs ABCDE e XABCDE.md` | Nota estratégica de decisão metodológica e fonte |
| `docs/auditoria-protocolo-aph.md` | Este relatório |

## Arquivos verificados sem alteração necessária

| Arquivo | Motivo |
|---|---|
| `CBAE - Trauma Cranioencefálico.md` | Não usa ABCDE como eixo |
| `CBAE - Trauma Musculoesquelético.md` | Não usa ABCDE como eixo |
| `CBAE - RCP - Ressuscitação Cardiopulmonar.md` | Protocolo próprio (BLS); não confunde com avaliação primária |
| `CBAE - Sinais Vitais.md` | Não usa ABCDE como eixo |
| `CBAE - Sistema de Atendimento Pré-Hospitalar.md` | Não usa ABCDE como eixo |
| `README.md`, `SOURCES.md`, `NOTICE.md` | Fora do escopo educacional da auditoria |

---

## Pontos de atenção

1. **Torniquete:** divergência significativa entre o vault e o manual. O vault ensinava torniquete como recurso válido; o manual afirma que não é abordado por ser técnica avançada. Mantido com ressalva.
2. **Biblioteca CBMSC online:** a página principal lista apenas categorias (11 manuais em APH). Não foi possível inspecionar títulos e conteúdos específicos sem acessar cada link interno — não há evidência de manual CBMSC com XABCDE, mas não há confirmação negativa exaustiva.
3. **Lacuna de AVDI no manual:** o manual não usa explicitamente a sigla AVDI (Alerta-Voz-Dor-Inconsciente) — essa sigla veio da apostila interna do projeto sem respaldo verificado. Mantida como mnemônico didático com ressalva.
4. **Sequência real do manual:** o manual coloca "nível de consciência" antes de "vias aéreas" — diferente do ABCDE clássico (que começa por A). Isso foi corrigido nas notas.

---

## Próximas revisões recomendadas

- Quando disponíveis os PDFs das demais categorias da biblioteca CBMSC (especialmente "Atendimento Pré-Hospitalar & Primeiros Socorros — 11 manuais"), verificar se algum usa XABCDE/ABCDE e se isso deveria alterar o vault.
- Revisar `CBAE - Afogamento.md`, `CBAE - Parto de Emergência.md` e `CBAE - Imobilização e Transporte.md` em auditoria futura para verificar se contêm referências a ABCDE.
- Criar banco de questões (`06 - Questões/`) quando disponível, garantindo que questões sobre avaliação da vítima usem a terminologia do Manual CBAE.
