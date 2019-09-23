# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angle = float(input('Digite o valor de um angulo qualquer: '))

senRadian = math.sin(math.radians(angle))
cosRadian = math.cos(math.radians(angle))
tangRadian = math.tan(math.radians(angle))

print('Com base no valor passado o valor de Seno é : {:.2f}'.format(senRadian))
print('Com base no valor passado o valor de Cosseno é : {:.2f}'.format(cosRadian))
print('Com base no valor passado o valor de Tangente é : {:.2f}'.format(tangRadian))
