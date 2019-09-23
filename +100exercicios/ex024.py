# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = input('Digite o nome da cidade: ').lower().strip().split()

First_word = city[0]

if First_word != 'santo':
    print(False)

else:
    print(True)
