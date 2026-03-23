# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Setup Ollama

```
1. Instalar o ollama
2. Baixe um modelo leve
3. Teste:
ollama run nome_modelo "Oi!"
```

## Estrutura Sugerida

```
src/
├── app.py # Aplicação principal (Streamlit)
```


## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas requests

# Rodar a aplicação
streamlit run .\src\app.py
```
