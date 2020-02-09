# Calculo de média ponderada de duas notas com dois pesos
#
# O calculo é feito pela multiplicação do peso1 e nota1 com a soma do peso2
# multiplicado pela nota2 e divido pela soma dos pesos.

peso1 = float(input('Digite o peso da primeira prova: '))
peso2 = float(input('Digie o peso da segunda prova: '))
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))

resultado = print('Sua média final é: ', (peso1*nota1) + (peso2*nota2) / (peso1+peso2))

input('Digite Enter Para Sair')
