# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

opposit = float(input('Digite o cateto oposto: '))
adjacent = float(input('Digite o cateto adjacente: '))

calc = (opposit**2) + (adjacent**2)

result = math.sqrt(calc)

print('A hipotenusa vai medir {0:.1f}'.format(result))
