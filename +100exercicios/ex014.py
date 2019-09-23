# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celToFah = [float(input('Celsius para Fahrenheit: '))]

print(list(map(lambda cel: (cel * 1.8) + 32, celToFah)))

FahToCel = [float(input('Fahrenheit para Celsius: '))]

print(list(map(lambda fah: (fah - 32) / 1.8, FahToCel)))
