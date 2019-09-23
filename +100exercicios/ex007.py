# Faça um programa que leia duas notas de um aluno. Calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota da primeira prova: '))
nota2 = float(input('Digite a segunda nota da segunda prova: '))

resultado = (nota1 + nota2) / 2

print('Sua média final é: {:.1f}'.format(resultado))
