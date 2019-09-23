# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

userDistance = float(input('Qual a distância da viagem?: '))

coast50km = 0.50
coast45km = 0.45

if userDistance < 200:
    coastTravel = userDistance * coast50km
    print('O valor da sua passagem é de: {:.2f}R$'.format(coastTravel))

elif userDistance > 200:
    coastTravel = userDistance * coast45km
    print('O valor da sua passagem é de: {:.2f}R$'.format(coastTravel))
