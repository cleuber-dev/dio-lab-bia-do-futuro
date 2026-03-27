# 💰 InvestIA – Educador Financeiro com IA

Projeto desenvolvido a partir do repositório base da DIO (BIA do Futuro), com adaptações e melhorias para criar um assistente inteligente focado em educação financeira.

## 🚀 Objetivo

O InvestIA tem como objetivo ajudar usuários a entender melhor suas finanças, oferecendo orientações simples e acessíveis sobre:

* Organização financeira
* Investimentos básicos
* Controle de gastos
* Planejamento financeiro

## 🧠 Tecnologias Utilizadas

* Python
* Ollama (execução local de modelos de IA)
* Streamlit (interface web)
* Git/GitHub

## ⚙️ Funcionalidades

* Chat interativo com IA
* Respostas voltadas para educação financeira
* Interface simples e intuitiva
* Personalização de respostas

## ▶️ Como Executar

### 🔹 Pré-requisitos

* Python instalado
* Ollama instalado e rodando localmente

Instale o Ollama:
[https://ollama.com](https://ollama.com)

Baixe um modelo (exemplo):

```bash
ollama pull llama3
```

### 🔹 Passos

1. Clone o repositório:

```bash
git clone https://github.com/cleuber-dev/dio-lab-bia-do-futuro.git
```

2. Acesse a pasta:

```bash
cd dio-lab-bia-do-futuro
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o projeto:

```bash
streamlit run app.py
```

## 🗂️ Estrutura do Projeto

```bash
dio-lab-bia-do-futuro/
│
├── README.md
├── src/
│   └── app.py
│
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
```

## 📌 Observações

* Este projeto é educacional
* Não substitui consultoria financeira profissional

## 👨‍💻 Autor

Desenvolvido por Cleuber Felix

---

💡 Projeto desenvolvido para fins de aprendizado e prática com IA e desenvolvimento de aplicações interativas.

