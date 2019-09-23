# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.

firstLine = float(input('Digite a primeira linha: '))
secoundLine = float(input('Digite a segunda linha: '))
thirthLine = float(input('Digite a terceira linha: '))

if firstLine < secoundLine + thirthLine and secoundLine < firstLine + thirthLine and thirthLine < firstLine + secoundLine:
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos não podem formar um triangulo')
