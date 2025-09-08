import streamlit as st

# Função para criptografar usando a Cifra de Vigenère
def vigenere_encrypt(message, key):
    encrypted_message = []
    key = key.upper()  # Transformar a chave em maiúsculas
    key_length = len(key)
    key_as_int = [ord(i) for i in key]  # Convertendo as letras da chave para valores numéricos
    message_int = [ord(i) for i in message.upper()]  # Convertendo a mensagem para valores numéricos

    for i in range(len(message_int)):
        if message[i].isalpha():  # Apenas letras serão criptografadas
            value = (message_int[i] + key_as_int[i % key_length]) % 26
            encrypted_message.append(chr(value + 65))  # Convertendo de volta para caractere
        else:
            encrypted_message.append(message[i])  # Mantém caracteres não-alfabéticos

    return ''.join(encrypted_message)

# Função para decriptografar usando a Cifra de Vigenère
def vigenere_decrypt(ciphertext, key):
    decrypted_message = []
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext.upper()]

    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            decrypted_message.append(chr(value + 65))
        else:
            decrypted_message.append(ciphertext[i])

    return ''.join(decrypted_message)

st.session_state.setdefault("mode", None)      # 'criptografado' | 'decriptografado' | None
st.session_state.setdefault("texto", "")

def mood(modo):
    chave = st.text_input("Informe a chave para criptografia")
    label = f"Informe o texto a ser {modo}"
    st.session_state.texto = st.text_input(label, key="text_input")

    # Ao pressionar Enter no text_input, o app reroda e este bloco mostra o resultado
    if modo == 'criptografado':
        result = vigenere_encrypt(st.session_state.texto, chave)
        titulo = f"Texto {modo}"

        if st.session_state.texto != "":
            st.success(f"{titulo}: {result}")

    if modo == 'descriptografado':
        result = vigenere_decrypt(st.session_state.texto, chave)
        titulo = f"Texto {modo}"

        if st.session_state.texto != "":
            st.success(f"{titulo}: {result}")

    return modo

def start_encrypt():
    st.session_state.mode = "criptografado"

def start_decrypt():
    st.session_state.mode = "descriptografado"



st.markdown("""
            # Cifra de Cesar
            ### O que é?
            """)

encode, decode = st.columns(2)
encode.button("Criptografar", on_click=start_encrypt)
decode.button("Descriptografar", on_click=start_decrypt)

if st.session_state.mode:
    mood(st.session_state.mode)
