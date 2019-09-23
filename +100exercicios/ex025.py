#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

Fullname = input('Digite o seu nome completo: ').lower().strip().split()

if 'silva' in Fullname:
    print(True)
else:
    print(False)
