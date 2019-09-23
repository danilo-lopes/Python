# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras possue (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

qtd_full_name = 0

name = input('Digite o seu nome completo: ')
print('Seu nome maisculo: {}'.format(name.upper()))
print('Seu nome minusculo: {}'.format(name.lower()))

for qtd in name.replace(' ', ''):
    qtd_full_name += 1

first_name = name.strip().split()[0]

print('O seu nome completo tem {} letras'.format(qtd_full_name))
print('O seu primeiro é {} e tem {} letras'.format(first_name, len(first_name)))
