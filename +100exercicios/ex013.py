# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Digite o seu salário R$: '))

calc = (15 * salary)/100
result = calc + salary

print('Você teve um aumento de 15% no seu salário. Você ganhava R$:{} e agora ganha R$:{}'.format(salary, result))
