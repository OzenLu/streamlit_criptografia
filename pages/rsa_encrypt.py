from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

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

"""
# Função principal
def main():
    # Gerar chaves
    private_key, public_key = generate_keys()

    # Exibir as chaves (opcional)
    pem_private_key, pem_public_key = serialize_keys(private_key, public_key)
    print("Chave privada:\n", pem_private_key.decode())
    print("Chave pública:\n", pem_public_key.decode())

    # Solicitar a mensagem do usuário
    message = input("Digite a mensagem que deseja criptografar: ")

    # Criptografar a mensagem
    encrypted_message = encrypt_message(public_key, message)
    print(f"\nMensagem criptografada: {encrypted_message}")

    # Decriptografar a mensagem
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print(f"\nMensagem decriptografada: {decrypted_message}")

# Executar o programa
if __name__ == "__main__":
    main()

"""