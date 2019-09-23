# Faça um programa que diga a partir de um número digitado, quem é o seu antecessor e o seu sucessor.

num = int(input('Digite um valor: '))

print('Analisando o valor {}, o seu antecessor é o número: {} e o seu sucessor é o número: {}'.format(num, (num-1), (num+1)))
