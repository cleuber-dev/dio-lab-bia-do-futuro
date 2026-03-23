import json
import pandas as pd
import requests
import streamlit as st

# ========== CARREGANDO OLLAMA ==========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "phi3"

# ========== CARREGANDO DADOS ==========
perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv', encoding='utf-8')
historico = pd.read_csv('./data/historico_atendimento.csv', encoding='utf-8')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))

# ========== MONTANDO O CONTEXTO ==========
contexto = f"""
USUÁRIO: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ========== SYSTEM PROMPT ==========
SYSTEM_PROMPT = """Você é o InvestIA, um educador financeiro amigável e didático de IA generativa.

Objetivo:

Ensinar conceitos de finanças pessoais e investimentos de forma simples, clara e acessível, explicando os diferentes
tipos de investimentos, suas vantagens e desvantagens, e comparando-os conforme o perfil de cada usuário.

Regras:

1. Nunca recomende investimentos específicos, apenas explique como funcionam  
2. Use os dados fornecidos pelo usuário para dar exemplos personalizados para ele 
3. Utilize linguagem simples, como se estivesse explicando para um amigo 
4. Se não souber algo, pode dizer: "Não tenho essa informação"
"""

# ========== CHAMANDO OLLAMA ==========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO USUÁRIO:
    {contexto}

    Prompt: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt":prompt, "stream": False})
    return r.json()['response']

# ========== INTERFACE STREAM LIST ==========
st.title("InvestAI está aqui para te auxiliar" )

if prompt := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(prompt)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(prompt))
