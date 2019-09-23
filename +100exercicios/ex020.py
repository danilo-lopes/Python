# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

count = 0
studants = []

while count < 4:
    studant = input('Digite o nome do aluno: ')
    studants.append(studant)
    count += 1

print('A ordem de apresentação é: {}'.format(sample(studants, k=4)))
