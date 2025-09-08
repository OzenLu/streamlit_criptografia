import streamlit as st

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The message to encrypt or decrypt.
        shift (int): The number of positions to shift the characters.
        mode (str): 'encode' to encrypt, 'decode' to decrypt.

    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
        elif 'A' <= char <= 'Z':
            start = ord('A')
        else:
            result += char
            continue

        if mode == 'codificado':
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
        elif mode == 'decodificado':
            shifted_char = chr(start + (ord(char) - start - shift) % 26)
        else:
            return "Invalid mode"
        result += shifted_char
    return result

def deslocamento():
    deslocamento = st.number_input("Insira um número para o deslocamento",
                                    format="%0.1f",
                                    value=None,
                                    placeholder="Insira um número inteiro")  

    st.write("O número de deslocamento é:", deslocamento)
    return deslocamento

st.session_state.setdefault("mode", None)      # 'codificado' | 'decodificado' | None
st.session_state.setdefault("deslocamento", 3)
st.session_state.setdefault("texto", "")

def start_encode():
    st.session_state.mode = "codificado"

def start_decode():
    st.session_state.mode = "decodificado"

st.markdown("""
            # Cifra de Cesar
            ### O que é?
            A Cifra de César é um tipo de cifra de substituição onde cada letra do texto é substituída por outra, que se encontra um número fixo de posições além dela no alfabeto. É considerada o primeiro método documentado de criptografia da história, tendo sido utilizada por Júlio César em suas comunicações militares.""")

encode, decode = st.columns(2)
encode.button("Codificar", on_click=start_encode)
decode.button("Decodificar", on_click=start_decode)

if st.session_state.mode:
    st.session_state.deslocamento = deslocamento()
    label = f"Insira o texto a ser {st.session_state.mode}"
    st.session_state.texto = st.text_input(label, key="text_input", value=st.session_state.texto)

    # Ao pressionar Enter no text_input, o app reroda e este bloco mostra o resultado
    if st.session_state.texto:
        try:
            result = caesar_cipher(st.session_state.texto, int(st.session_state.deslocamento), st.session_state.mode)
            titulo = f"Texto {st.session_state.mode}"
            st.success(f"{titulo}: {result}")
        except:
            st.write("Informe o número de deslocamento")