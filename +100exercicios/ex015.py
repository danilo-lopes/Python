# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

days = input('Dias de aluguel do carro: ')
usedKM = float(input('Kilometros rodados: '))

resultKM = usedKM * 0.15
resultDays = 60 * float(days)

print('Você usou o carro por {} dias. Sua fatura é de: R${} reais'.format(days, (resultKM + resultDays)))
