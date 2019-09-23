# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

carVelocity = float(input('Qual a velocidade atual do carro?: '))
kmLimit = float(80)

if carVelocity > 80:
    priceMult = (carVelocity - kmLimit) * 7
    print('{}km/h ultrapassa o limite permitido de 80km/h. Sendo assim você foi multado. Valor: R${:.2f}'.format(
        carVelocity, priceMult))
else:
    print('{}km/h está dentro do limite permitido de 80km/h'.format(carVelocity))
