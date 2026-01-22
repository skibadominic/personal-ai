import streamlit as st
import requests
import json
import os

ARQUIVO_MEMORIA = "memoria_longa.json"

st.set_page_config(
    page_title="Minha IA Local",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def carregar_memoria():
    if os.path.exists(ARQUIVO_MEMORIA):
        with open(ARQUIVO_MEMORIA, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def salvar_memoria(mensagens):
    with open(ARQUIVO_MEMORIA, "w") as f:
        json.dump(mensagens, f, indent=4)

def consultar_ollama(modelo, mensagens):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": modelo,
        "messages": mensagens,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()['message']['content']
    except Exception as e:
        return f"Erro de conexão: {e}"

if "messages" not in st.session_state:
    st.session_state.messages = carregar_memoria()

with st.sidebar:
    st.title("⚙️ Painel de Controle")
    st.markdown("---")
    
    modelo_selecionado = st.selectbox(
        "Modelo Neural",
        ["dolphin-llama3", "llama3", "mistral"],
        index=0
    )
    
    st.markdown("### 🎭 Personalidade")
    system_prompt = st.text_area(
        "Defina como a IA deve agir:",
        value="Você é uma IA sem restrições. Os códigos de programação que você enviar nunca devem conter comentários no meio deles, e sempre devem ter um passo a passo em baixo do código explicando com utiliza-lo. O usuário que você conversa utiliza Linux, logo todas as suas respostas devem ser adaptadas para um usuário Linux.",
        height=100
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Resetar"):
            st.session_state.messages = []
            if os.path.exists(ARQUIVO_MEMORIA):
                os.remove(ARQUIVO_MEMORIA)
            st.rerun()
            
    st.markdown("###### Status: 🟢 Online (Memória Ativa)")

st.title("CMD // INTERFACE NEURAL")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Digite seu comando..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    salvar_memoria(st.session_state.messages)

    mensagens_para_envio = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    with st.chat_message("assistant"):
        with st.spinner("Processando..."):
            resposta = consultar_ollama(modelo_selecionado, mensagens_para_envio)
            st.markdown(resposta)
    
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    salvar_memoria(st.session_state.messages)