---
tipo: auditoria-gabaritos
criado: 2026-04-29
status: concluído
tags: [questões, gabarito, auditoria, qualidade, manutenção]
fonte: Simulados 01-03
---

# Auditoria de Gabaritos e Qualidade das Questões

> Esta nota registra a auditoria de 2026-04-29 que corrigiu o viés sistemático de gabarito no banco de questões do BC 2026.

## Diagnóstico — Causa Raiz

O banco de 100 questões (Simulados 01, 02, 03) apresentava concentração crítica na letra B:

| Letra | Antes | Depois |
|:---:|---:|---:|
| A | 25% | **20%** |
| B | **56%** ⚠️ | **20%** ✅ |
| C | 13% | **20%** |
| D | 5% | **20%** |
| E | 1% | **20%** |

**Padrões adicionais detectados:**
- Alternativa correta = mais longa em 65% das questões (caiu para 58% após reescrita)
- Distratores usando absolutismo (`somente`, `apenas`, `nunca`) vs. linguagem moderada da correta (`conforme`, `entre outros`)
- Distratores de domínios completamente errados (termos de Português em questões de CIE, "literatura brasileira" em questão de extinção)

**Causa raiz:** viés editorial humano + ausência de salvaguardas processuais (sem template, sem auditoria automatizada, sem contrato de agente).

## Solução Aplicada

### 1. Script de auditoria (`scripts/auditoria_gabaritos.py`)

```bash
# Auditoria (dry-run)
python3 scripts/auditoria_gabaritos.py --audit

# Rebalancear gabaritos
python3 scripts/auditoria_gabaritos.py --shuffle --seed 42 --write

# Auto-teste do script
python3 scripts/auditoria_gabaritos.py --self-test
```

O script parseia os simulados, detecta problemas de qualidade e pode rebalancear alternativas preservando o conteúdo correto por hash SHA-1.

### 2. Rebalanceamento dos simulados (seed 42)

Cada simulado rebalanceado para 20% por letra — `--shuffle --seed 42 --write` — produzindo distribuição perfeita: A=B=C=D=E=7 questões em cada simulado de 35; A=B=C=D=E=6 em cada de 30.

### 3. Reescrita de distratores absurdos

Questões com distratores caricatos substituídas por alternativas plausíveis do mesmo domínio:

| Simulado | Q | Distrator removido | Substituído por |
|---|:---:|---|---|
| Sim 01 | Q01 | `na alternativa mais extensa` | `na interpretação que mais agrada ao leitor` |
| Sim 01 | Q20 | `aumentam a cor da mangueira` | `ampliam permanentemente a pressão de serviço` |
| Sim 01 | Q27 | `apenas tipo sanguíneo` / `somente altura e peso` / `apenas nível de escolaridade` / `somente histórico familiar` | Subconjuntos plausíveis de sinais vitais |
| Sim 01 | Q28 | `oferecer bebida alcoólica` | `administrar leite para neutralizar o veneno` |
| Sim 01 | Q30 | `somente treinamento físico` / `apenas curso superior` / `somente CIE` / `apenas estágio operacional` | Variações de cursos com horas incorretas |
| Sim 02 | Q09 | `nome do fabricante` / `cor da parede` / `se há literatura no local` | Atributos plausíveis mas insuficientes do extintor |
| Sim 02 | Q22 | `professor de literatura` / `apenas agente de trânsito` | Perfis plausíveis mas incorretos para CFBC |
| Sim 02 | Q28 | `criar conteúdo de Português` / `substituir leis de trânsito` | Competências reais mas erradas da IG |
| Sim 03 | Q08 | `figuras de linguagem` / `cursos comunitários` | Categorias legais plausíveis do CTB |
| Sim 03 | Q10 | `literatura brasileira` / `informática avançada` / `mergulho profissional` | Categorias de CNH próximas à correta |
| Sim 03 | Q14 | `formas verbais` / `sinais vitais` | Equipamentos/métodos do Manual CIE |
| Sim 03 | Q16 | `resfriamento, literatura e semântica` | Conceitos técnicos de CIE |
| Sim 03 | Q19 | `discutir gabarito` / `avaliar literatura brasileira` | Técnicas incorretas mas de APH |
| Sim 03 | Q23 | `candidato aprovado em literatura` | `profissional concursado para cargo de apoio municipal` |
| Sim 03 | Q28 | `criar questões de literatura` | `registrar ocorrências de trânsito do voluntário` |

### 4. Salvaguardas processuais

- Criados `_Templates/Questão.md` e `_Templates/Simulado.md` com checklist anti-viés
- Criado `AGENTS.md` na raiz com regras para agentes AI
- Criado `docs/adr/ADR-001-auditoria-gabaritos.md` com a decisão arquitetural

## Como Rodar a Auditoria

```bash
# Da raiz do repositório:
python3 scripts/auditoria_gabaritos.py --audit
```

Saída: `docs/relatorios/auditoria-gabaritos-AAAA-MM-DD.md` e `.json`.

**Exit code 0** = sem violações bloqueantes.
**Exit code 1** = há violações (ver seção "Critérios de falha" no relatório).

## Como Interpretar o Relatório

| Métrica | Verde ✅ | Amarelo 🟡 | Vermelho 🔴 |
|---|---|---|---|
| % por letra | 15–25% | 10–15% ou 25–30% | <10% ou ≥30% |
| Correta = mais longa | <30% | 30–50% | >50% |
| Absolutismo em erradas | <20% | 20–40% | >40% |
| Problemas críticos | 0 | — | >0 |

## Pendências e Próximos Passos

- [ ] **"Correta = mais longa" ainda em 58%**: as questões restantes têm resposta genuinamente mais longa por conteúdo técnico. Solução futura: ao criar novas questões, normalizar comprimento de alternativas como parte do checklist.
- [ ] **Criar Simulado 04** usando `_Templates/Simulado.md` e rodar `--audit` antes de salvar.
- [ ] **Integrar `--audit` como hook de pré-commit**: adicionar ao `.git/hooks/pre-commit` quando o fluxo de edição estiver estável.
- [ ] **Campos faltantes**: adicionar `fonte_especifica` (lei + artigo) e `id` estável por questão para rastreio de embaralhamento histórico.

## Conexões

- [[_Banco de Questões]]
- [[Gabaritos Comentados]]
- [[Simulado 01 - Diagnóstico]]
- [[Simulado 02 - Conhecimentos Específicos]]
- [[Simulado 03 - Reta Final]]
- [[Plano de Simulados]]
