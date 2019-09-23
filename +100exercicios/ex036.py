# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

houseValue = float(input('Digite o valor da casa: '))
userSalary = float(input('Digite o seu salario: '))
yearsToPay = int(input('Quantos anos de financiamento?: '))

monthToPay = yearsToPay * 12
valueToUse = userSalary * 0.30

value = valueToUse * monthToPay

if value < houseValue:
    print('Emprestimo Negado. Em {} anos você só consegue pagar {}'.format(yearsToPay, value))
    print('Você precisa dar uma entrada de {}'.format(houseValue - value))

else:
    print('Emprestimo Concedido. Em {} anos você consegue pagar'.format(yearsToPay))
