import streamlit as st
from pages.caesar_cipher import caesar_cipher
from pages.vigenere_encrypt import vigenere_encrypt, vigenere_decrypt


st.set_page_config(page_title="App de Criptografia", page_icon='🔐')

st.markdown("""
            # Bem vindo!
            ## Aplicativo de Criptografias

            Aplicativo com intuito de demonstrar alguns tipos de criptografia
            """)