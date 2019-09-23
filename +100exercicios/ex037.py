# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


def intToBin(number):
    if number == 0:
        return [0]

    bit = []

    while number:
        bit.append(number % 2)
        number >>= 1

    return bit[:: - 1]


number = int(input('Digite um número: '))

print(intToBin(number))
