# Crie um programa que leia um número e mostre o seu dobro, tripo e raiz quadrada.

numero = int(input('Digite um número: '))

primeiro = numero * 2
segundo = numero * 3
terceiro = (numero ** (1/2))

print('Dobro do número é: {}'.format(primeiro))
print('O triplo do número é: {}'.format(segundo))
print('A raiz quadrada do número é: {}'.format(terceiro))
