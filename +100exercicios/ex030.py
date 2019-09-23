# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

userNumber = int(input('Digite um número: '))

print('Impar' if userNumber % 2 != 0 else 'Par')

if userNumber % 2 == 0:
    print('O número {} é par'.format(userNumber))
else:
    print('O número {} é impar'.format(userNumber))
