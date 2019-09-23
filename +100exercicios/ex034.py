# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Digite o seu salário: '))

if salary > 1250.00:
    calc = (salary * 0.10) + salary
    print('Você teve um aumento de 10%. Sendo assim o seu salário vai de R${} para R${}'.format(salary, calc))

elif salary < 1250.00:
    calc = (salary * 0.15) + salary
    print('Você teve um aumento de 15%. Sendo assim o seu salário vai de R${} para {}'.format(salary, calc))
