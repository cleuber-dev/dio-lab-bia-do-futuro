# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no InvestIA |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar explicações para didática do usuário |
| `produtos_financeiros.json` | JSON |Conhecer os produtos finaceiros para poder apresentar ao usuário |
| `transacoes.csv` | CSV | Analisar os padrões do usuário para poder educar da melhor forma possível |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Foram acrescentados novos produtos financeiros, aumentando assim o database do agente que é focado em investimentos.
Com isso o InvestIA estará mais apto a educar o cliente de forma mais acertiva.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos da base de conhecimento serão carregado via código em linguagem python como mostrado a seguir:

```python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

De forma simplificada, simplismente podemos "injetar" os dados para formar o prompt. No caso de soluções mais robustas,
o melhor seria utilizar o código para se ganhar flexibiliade.

```text
DADOS E PERFIL DO USUÁRIO data/perfil_investidor.json:

Nome: João Silva
Idade: 32 anos
Profissão: Analista de Sistemas
Renda mensal: R$ 5.000,00
Perfil de investidor: moderado
Objetivo principal: Construir reserva de emergência
Patrimônio total: R$ 15.000,00
Reserva de emergência atual: R$ 10.000,00
Aceita risco: não

Metas:

Completar reserva de emergência
Valor necessário: R$ 15.000,00
Prazo: 06/2026

Entrada do apartamento
Valor necessário: R$ 50.000,00
Prazo: 12/2027

TRANSAÇÕES DO USUÁRIO data/transacoes.csv:

01/10/2025 – Salário
Categoria: receita
Tipo: entrada
Valor: R$ 5.000,00

02/10/2025 – Aluguel
Categoria: moradia
Tipo: saída
Valor: R$ 1.200,00

03/10/2025 – Supermercado
Categoria: alimentação
Tipo: saída
Valor: R$ 450,00

05/10/2025 – Netflix
Categoria: lazer
Tipo: saída
Valor: R$ 55,90

07/10/2025 – Farmácia
Categoria: saúde
Tipo: saída
Valor: R$ 89,00

10/10/2025 – Restaurante
Categoria: alimentação
Tipo: saída
Valor: R$ 120,00

12/10/2025 – Uber
Categoria: transporte
Tipo: saída
Valor: R$ 45,00

15/10/2025 – Conta de Luz
Categoria: moradia
Tipo: saída
Valor: R$ 180,00

20/10/2025 – Academia
Categoria: saúde
Tipo: saída
Valor: R$ 99,00

25/10/2025 – Combustível
Categoria: transporte
Tipo: saída
Valor: R$ 250,00

HISTÓRICO DE ATENDIMENTO DO USUÁRIO data/historico_atendimento.csv:

15/09/2025 – Canal: chat
Tema: CDB
Resumo: Cliente perguntou sobre rentabilidade e prazos
Resolvido: sim

22/09/2025 – Canal: telefone
Tema: Problema no app
Resumo: Erro ao visualizar extrato foi corrigido
Resolvido: sim

01/10/2025 – Canal: chat
Tema: Tesouro Selic
Resumo: Cliente pediu explicação sobre o funcionamento do Tesouro Direto
Resolvido: sim

12/10/2025 – Canal: chat
Tema: Metas financeiras
Resumo: Cliente acompanhou o progresso da reserva de emergência
Resolvido: sim

25/10/2025 – Canal: email
Tema: Atualização cadastral
Resumo: Cliente atualizou e-mail e telefone
Resolvido: sim

PRODUTOS ADEQUADOS PARA APRENDIZADO data/produtos_financeiros.json: 

Tesouro Selic
Categoria: renda fixa
Risco: baixo
Rentabilidade: 100% da Selic
Aporte mínimo: R$ 30,00
Indicado para: Reserva de emergência e iniciantes

CDB Liquidez Diária
Categoria: renda fixa
Risco: baixo
Rentabilidade: 102% do CDI
Aporte mínimo: R$ 100,00
Indicado para: Quem busca segurança com rendimento diário

LCI/LCA
Categoria: renda fixa
Risco: baixo
Rentabilidade: 95% do CDI
Aporte mínimo: R$ 1.000,00
Indicado para: Quem pode esperar 90 dias (isento de IR)

Fundo Multimercado
Categoria: fundo
Risco: médio
Rentabilidade: CDI + 2%
Aporte mínimo: R$ 500,00
Indicado para: Perfil moderado que busca diversificação

Fundo de Ações
Categoria: fundo
Risco: alto
Rentabilidade: variável
Aporte mínimo: R$ 100,00
Indicado para: Perfil arrojado com foco no longo prazo

Tesouro IPCA+
Categoria: renda fixa
Risco: baixo
Rentabilidade: IPCA + taxa prefixada
Aporte mínimo: R$ 30,00
Indicado para: Proteção contra inflação no longo prazo

Tesouro Prefixado
Categoria: renda fixa
Risco: baixo
Rentabilidade: taxa fixa anual
Aporte mínimo: R$ 30,00
Indicado para: Quem acredita na queda da taxa de juros

Debêntures
Categoria: renda fixa
Risco: médio
Rentabilidade: CDI + taxa ou prefixada
Aporte mínimo: R$ 1.000,00
Indicado para: Investidor que busca maior retorno aceitando risco de crédito

CRI/CRA
Categoria: renda fixa
Risco: médio
Rentabilidade: CDI + taxa ou IPCA + taxa
Aporte mínimo: R$ 1.000,00
Indicado para: Investidor que busca isenção de IR com prazo maior

ETF de Índice (ex: BOVA11)
Categoria: renda variável
Risco: médio
Rentabilidade: acompanha o índice (ex: Ibovespa)
Aporte mínimo: R$ 100,00
Indicado para: Quem quer diversificação com baixo custo

Ações Individuais
Categoria: renda variável
Risco: alto
Rentabilidade: variável
Aporte mínimo: R$ 50,00
Indicado para: Investidor com conhecimento e foco no longo prazo

Fundos Imobiliários (FIIs)
Categoria: renda variável
Risco: médio
Rentabilidade: dividendos + valorização
Aporte mínimo: R$ 100,00
Indicado para: Renda passiva mensal isenta de IR

Previdência Privada (PGBL/VGBL)
Categoria: previdência
Risco: baixo
Rentabilidade: depende do fundo
Aporte mínimo: R$ 100,00
Indicado para: Planejamento de aposentadoria e benefício fiscal

COE (Certificado de Operações Estruturadas)
Categoria: estruturado
Risco: médio
Rentabilidade: atrelado a cenários de mercado
Aporte mínimo: R$ 1.000,00
Indicado para: Quem busca retornos diferenciados com proteção parcial

Conta Remunerada
Categoria: renda fixa
Risco: baixo
Rentabilidade: 100% do CDI
Aporte mínimo: R$ 1,00
Indicado para: Liquidez diária com rendimento automático

```
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo abaixo apresenta-se como um resumo dos dados originais.

```
DADOS DO USUÁRIO:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

RESUMO DE GASTOS DO USUÁRIO:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

PRODUTOS ADEQUADOS PARA APRENDIZADO:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Multimercado (risco médio)
- Fundo de Ações (risco alto)
- Tesouro IPCA+ (risco baixo)
- Tesouro Prefixado (risco baixo)
- Debêntures (risco médio)
- CRI/CRA (risco médio)
- ETF de Índice (ex: BOVA11) (risco médio)
- Ações Individuais (risco alto)
- Fundos Imobiliários (FIIs) (risco médio)
- Previdência Privada (PGBL/VGBL) (risco baixo)
- COE (Certificado de Operações Estruturadas) (risco médio)
- Conta Remunerada (risco baixo)
...
```
