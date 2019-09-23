# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

userNumber = int(input('Tente advinhar o número que eu processei: '))

ramdomicNumber = randint(0, 5)

if userNumber == ramdomicNumber:
    print('Eu pensei no número {} e você digitou o número {}. Parabéns, você acertou!'.format(ramdomicNumber, userNumber))

else:
    print('Eu pensei no número {} e você digitou o número {}. Errou!'.format(ramdomicNumber, userNumber))
