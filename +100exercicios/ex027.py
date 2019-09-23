# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

name = input('Digite: ').strip().split()

print('O seu primeiro nome é {} e o seu ultimo nome é {}'.format(name[0], name[:: -1][0]))
