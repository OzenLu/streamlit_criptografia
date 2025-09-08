import string

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

# Teste da máquina Enigma
"""
message = input("Digite uma mensagem para ser criptografada: ")
plugboard_pairs = [('A', 'B'), ('C', 'D')]  # Configuração do painel de conectores
encrypted_message = enigma(message, plugboard_pairs)

print("Mensagem Original: ", message)
print("Mensagem Encriptada: ", encrypted_message)
"""
