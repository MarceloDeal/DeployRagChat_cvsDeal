import streamlit as st
import json
import os

# Função para carregar dados de login do arquivo JSON
def load_login_data():
    try:
        with open('manutencao/prop.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Erro ao carregar os dados de login: {e}")
        return {}

# Função para verificar credenciais
def check_credentials(username, password, login_data):
    if username in login_data and login_data[username] == password:
        return True
    return False

# Página de login
def login_page():
    st.image("img/logodeal.jpg", width=200) 
    st.title("Login - Deal Talent")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type='password')
    login_data = load_login_data()

    if st.button("Login"):
        if check_credentials(username, password, login_data):
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.error("Nome de usuário ou senha incorretos")

# Página home
def home_page():
    st.title("DEAL TALENT - AVALIAÇÃO DE PERFIS")
    try:
        with open("Home.py", 'r', encoding='utf-8') as f:
            exec(f.read(), globals())
    except FileNotFoundError:
        st.error("Arquivo home.py não encontrado.")
    except Exception as e:
        st.error(f"Erro ao carregar o conteúdo da página home: {e}")

# Verifica se o usuário está autenticado e carrega a página apropriada
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if st.session_state['authenticated']:
    home_page()
else:
    login_page()
