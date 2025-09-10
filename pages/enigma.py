import string
import streamlit as st

# Definindo o alfabeto e os rotores
ALPHABET = string.ascii_uppercase
ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Inicialização da configuração inicial dos rotores
ROTORS = [ROTOR_I, ROTOR_II, ROTOR_III]

# Função para criar o plugboard (painel de conectores)
def create_plugboard(pairs):
    plugboard = {c: c for c in ALPHABET}  # Mapeamento inicial sem alteração
    for a, b in pairs:
        plugboard[a] = b
        plugboard[b] = a
    return plugboard

# Função para girar o rotor
def rotate(rotor):
    return rotor[1:] + rotor[0]

# Função de substituição de um único caractere pelo rotor
def substitute(rotor, c, reverse=False):
    if reverse:
        return ALPHABET[rotor.index(c)]
    else:
        return rotor[ALPHABET.index(c)]

# Função principal para encriptar uma mensagem
def enigma(message, plugboard_pairs):
    plugboard = create_plugboard(plugboard_pairs)
    encrypted_message = []

    # Para cada caractere na mensagem
    for char in message.upper():
        if char not in ALPHABET:
            encrypted_message.append(char)
            continue

        # Passo 1: Plugboard
        char = plugboard[char]

        # Passo 2: Passar pelos rotores da direita para a esquerda
        for i, rotor in enumerate(ROTORS):
            char = substitute(rotor, char)
            # Rodar o rotor I a cada letra, o II a cada 26 letras
            if i == 0 or (i == 1 and len(encrypted_message) % 26 == 0):
                ROTORS[i] = rotate(rotor)

        # Passo 3: Refletor
        char = substitute(REFLECTOR, char)

        # Passo 4: Voltar pelos rotores da esquerda para a direita
        for rotor in reversed(ROTORS):
            char = substitute(rotor, char, reverse=True)

        # Passo 5: Plugboard
        char = plugboard[char]

        encrypted_message.append(char)

    return ''.join(encrypted_message)

st.markdown("""
            # Máquina Enigma
            ### O que é?

            Enigma foi uma máquina eletromecânica de criptografia com rotores. Utilizada tanto para criptografar como para descriptografar códigos de guerra, foi usada de várias formas na Europa a partir dos anos 1920.

            ### Como funciona?

            Tal como outras máquinas com rotores, a Máquina Enigma é uma combinação de sistemas mecânicos e elétricos. O mecanismo consiste num teclado, num conjunto de discos rotativos chamados rotores, dispostos em fila; e de um mecanismo de avanço que faz andar alguns rotores uma posição quando uma tecla é pressionada. O mecanismo varia entre diversas versões da máquina, mas o mais comum é o rotor colocado à direita avançar uma posição com cada tecla premida, e ocasionalmente despoletar o movimento rotativo dos restantes rotores, à sua esquerda, à semelhança do mecanismo conta-quilómetros de um automóvel. O movimento contínuo dos rotores provoca diferentes combinações na criptografia.
            """)

st.image("https://upload.wikimedia.org/wikipedia/commons/0/0a/Enigma_Machine_at_NSA.jpg", caption="Máquina Enigma com três rotores, teclado, luzes e conexões para câmbio de codificação", width="stretch")

message = st.text_input("Digite uma mensagem para ser criptografada")

plugboard_pairs = [('A', 'B'), ('C', 'D')]
if message:
    st.success(f"Mensagem criptografada: {enigma(message, plugboard_pairs)}")
    st.success(f"Mensagem Original: {message}")
