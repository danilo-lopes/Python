# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome dos alunos e escrevendo na tela o nome do escolhido.
import random

count = 0
studants = []

while count < 4:
    studant = input('Digite o nome do aluno: ')
    studants.append(studant)
    count += 1

print('Quem vai apagar a lousa vai ser o aluno: {}'.format(random.choice(studants)))
