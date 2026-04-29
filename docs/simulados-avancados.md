# Simulados avançados

## Objetivo

Os simulados avançados transformam as questões do vault em rotina de medição,
correção e replanejamento. A meta não é decorar gabarito, mas identificar
lacunas reais dentro do edital.

## Tipos de simulado

- Diagnóstico: mede o nível geral e mostra prioridades iniciais.
- Específico: concentra o bloco de maior peso ou a disciplina mais fraca.
- Reta final: simula pressão, tempo e pegadinhas prováveis.

## Cronômetro

Use cronômetro para aproximar o treino da prova. Registre tempo total, tempo
médio por questão e questões deixadas em dúvida.

Se o desempenho cair por pressa, reduza velocidade. Se cair por falta de
conteúdo, volte para a nota atômica e flashcards.

## Registro de desempenho

Depois de cada simulado:

1. corrija todas as questões;
2. calcule acertos por disciplina;
3. registre erros relevantes;
4. relacione cada erro à nota atômica;
5. atualize a matriz de desempenho;
6. defina a próxima revisão.

## Análise de erros

Classifique cada erro:

- conceito ausente;
- confusão entre alternativas;
- leitura apressada;
- esquecimento;
- pegadinha de nomenclatura;
- insegurança por falta de revisão.

Cada erro relevante deve gerar uma ação: revisar nota, criar flashcard,
refazer questão parecida ou estudar a fonte oficial.

## Repetição sem decorar

Não repita o mesmo simulado imediatamente. Antes de repetir:

- corrija os erros;
- revise notas relacionadas;
- espere um intervalo;
- misture questões de temas diferentes;
- compare desempenho por disciplina, não só o total.

## Novos simulados

Crie novos simulados a partir do banco de questões respeitando:

- edital;
- distribuição de disciplinas;
- 5 alternativas;
- uma única correta;
- fonte e nota relacionada;
- linguagem objetiva;
- ausência de conteúdo externo como fonte principal.

**Anti-viés obrigatório:** após criar o simulado, rodar a auditoria para garantir distribuição equilibrada de gabaritos:

```bash
python3 scripts/auditoria_gabaritos.py --audit
# Exit 0 = pronto para usar. Exit 1 = corrigir concentração de letra antes.
```

Use `_Templates/Simulado.md` para estrutura com checklist integrado. Ver [[Auditoria de Gabaritos e Qualidade das Questões]] para contexto completo.

## Faixas de desempenho

| Faixa | Interpretação | Ação |
|---|---|---|
| Abaixo de 60% | Base instável | Revisar fundamentos e refazer flashcards |
| 60% a 75% | Lacunas claras | Corrigir erros por disciplina |
| 75% a 85% | Bom domínio com perdas pontuais | Treinar tempo e pegadinhas |
| Acima de 85% | Domínio forte | Manutenção, revisão e simulados cronometrados |
