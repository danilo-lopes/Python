# Capturar do terminal 3 argumentos
# um que sera uma palavra, outro que sera um comando para criptografar ou decriptar
# outro que sera a chave da criptografia

# ex: python pedro encrypt 1
# saida: qfesp
# terminal: ./script.py mensagem cript/decript chave

import sys

alphabet = list('abcdefghijklmnoprstuvwxyz')

message = list(sys.argv[1])
command = sys.argv[2]
key = int(sys.argv[3])


def decrypt(message, key):
    decryptedWord = []

    for character in message:
        charOnAlphabet = alphabet.index(character)

        if (charOnAlphabet + key) >= len(alphabet):
            returnedCharAlphabet = len(alphabet) - (charOnAlphabet + key)
            decryptedWord.append(alphabet[returnedCharAlphabet])

        else:
            decryptedWord.append(alphabet[charOnAlphabet - key])
    return decryptedWord


def encrypt(message, key):
    encryptedWord = []

    for character in message:
        charOnAlphabet = alphabet.index(character)

        if (charOnAlphabet + key) >= len(alphabet):
            returnedCharAlphabet = len(alphabet) - (charOnAlphabet + key)
            encryptedWord.append(alphabet[returnedCharAlphabet])

        else:
            encryptedWord.append(alphabet[charOnAlphabet + key])

    return encryptedWord


for character in message:
    if command == 'encrypt':
        result = encrypt(message, key)

    if command == 'decrypt':
        result = decrypt(message, key)

print('Texto:')
print(''.join(result))
