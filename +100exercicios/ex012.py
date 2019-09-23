#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

value = float(input('Digite o preço do produto R$: '))

descont = (5 * value)/100
result = value - descont

print('O produto teve 5% de desconto. Sendo assim você irá pagar {0:.2f} por ele.'.format(result))
