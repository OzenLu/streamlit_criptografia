from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import streamlit as st

# Função para gerar as chaves RSA (pública e privada)
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Função para criptografar a mensagem usando a chave pública
def encrypt_message(public_key, message):
    encrypted_message = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message

# Função para decriptografar a mensagem usando a chave privada
def decrypt_message(private_key, encrypted_message):
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode('utf-8')

# Função para serializar a chave privada e pública (opcional: salvar as chaves em arquivos)
def serialize_keys(private_key, public_key):
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem_private_key, pem_public_key

st.session_state.setdefault("texto", "")
st.session_state.setdefault("private_key", "")
st.session_state.setdefault("public_key", "")

def mood(modo, private_key, public_key):
    label = f"Informe o texto a ser {modo}"
    st.session_state.texto = st.text_input(label, key="text_input")

    # Ao pressionar Enter no text_input, o app reroda e este bloco mostra o resultado
    if modo == 'criptografado':
        st.write(public_key)
        result = encrypt_message(public_key ,st.session_state.texto)
        titulo = f"Texto {modo}"

        if st.session_state.texto != "":
            st.success(f"{titulo}: {result}")

    if modo == 'descriptografado':
        result = decrypt_message(private_key, st.session_state.texto)
        titulo = f"Texto {modo}"

        if st.session_state.texto != "":
            st.success(f"{titulo}: {result}")

    return modo

def gerar_chaves():
    st.session_state.private_key, st.session_state.public_key = generate_keys()

st.markdown("""
            # Criptografia RSA
            ### O que é?

            **RSA (Rivest-Shamir-Adleman)** é um dos primeiros sistemas de criptografia de chave pública e é amplamente utilizado para transmissão segura de dados. Neste sistema de criptografia, a chave de encriptação é pública e é diferente da chave de decriptação que é secreta (privada). Um usuário do **RSA** cria e publica uma chave (chave pública) baseada em dois números primos grandes, junto com um valor auxiliar. Os números primos devem ser mantidos secretos.

            ### Como funciona?

            O RSA envolve um par de chaves, uma chave pública que pode ser conhecida por todos e uma chave privada que deve ser mantida em sigilo. Toda mensagem cifrada usando uma chave pública só pode ser decifrada usando a respectiva chave privada. A criptografia RSA atua diretamente na internet, por exemplo, em mensagens de emails, em compras on-line e o que você imaginar; tudo isso é encriptado e decriptado pela criptografia RSA.
            """)

st.image("https://tse1.mm.bing.net/th/id/OIP.-cWt7M0nTFV32RbGdbUutgHaE4?rs=1&pid=ImgDetMain&o=7&rm=3", caption="Funcionamento RSA", width="stretch")

click = st.button("Gerar chaves", on_click=gerar_chaves, width="stretch")

if click:
    pem_private_key, pem_public_key = serialize_keys(st.session_state.private_key, st.session_state.public_key)
    st.write("Chave privada:\n\n", pem_private_key.decode())
    st.write("Chave pública:\n\n", pem_public_key.decode())

message = st.text_input("Digite uma mensagem para ser criptografada")

if message:
    encrypted_message = encrypt_message(st.session_state.public_key, message)
    decrypted_message = decrypt_message(st.session_state.private_key, encrypted_message)
    st.success(f"Mensagem criptograda: {encrypted_message}")
    st.success(f"Mensagem descriptograda: {decrypted_message}")
