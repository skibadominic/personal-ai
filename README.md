# 🧠 Neural Interface // Local AI

> Uma interface de Inteligência Artificial rodando 100% localmente, focada em privacidade, sem filtros corporativos e com persistência de memória.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Ollama](https://img.shields.io/badge/Backend-Ollama-black)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

## 📋 Sobre o Projeto

Este projeto consiste em uma implementação Full-Stack de um assistente de IA pessoal. Diferente de soluções comerciais (ChatGPT, Gemini), todo o processamento ocorre no próprio hardware do usuário ou em um servidor doméstico, garantindo que nenhum dado deixe a rede local.

### Principais Funcionalidades
- **Totalmente Offline:** Utiliza a API local do [Ollama](https://ollama.com/) para inferência.
- **Sem Censura:** Projetado para rodar modelos "uncensored" (como Dolphin-Llama3), removendo barreiras de alinhamento corporativo.
- **Memória Persistente:** Sistema de logs em JSON que permite à IA "lembrar" de conversas passadas mesmo após reinicialização.
- **Interface Cyberpunk:** Frontend desenvolvido em Streamlit com tema dark mode customizado e responsivo.
- **Arquitetura Flexível:** Pode rodar em GPUs High-End (RTX 4070+) ou ser adaptado para CPUs antigas (via modelos quantizados como Qwen/Phi-3).

## 🛠️ Tech Stack

* **Linguagem:** Python
* **Interface:** Streamlit
* **LLM Engine:** Ollama
* **Modelos Testados:**
    * `dolphin-llama3` (Para Hardware com GPU dedicada)
    * `qwen2.5:0.5b` (Para Servidores CPU/Low-end)

## 🚀 Como Rodar

### Pré-requisitos
1.  **Linux** (Ubuntu/Debian/Fedora)
2.  **Python 3.10+**
3.  **Ollama** instalado e rodando (`curl -fsSL https://ollama.com/install.sh | sh`)

### Instalação

```bash
# 1. Clone o repositório
git clone [https://github.com/SEU_USUARIO/minha-ia-local.git](https://github.com/SEU_USUARIO/minha-ia-local.git)
cd minha-ia-local

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt
