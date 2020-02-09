##Crie um código que pegue o nome do aluno, a nota da primeira prova, nota da segunda prova e
##a quantidade de faltas que o aluno teve.
##
##Mostre se o aluno passou por média e falta, reprovou por falta ou reprovou por média.
##Considerando que a média é 6 e a assiduidade é de 70%


nome=input('Digite o nome do aluno: ')

valid_nota=False

while valid_nota==False:
    nota1=input('Digite a nota da primeira prova: ')
    try:
        nota1=float(nota1)
        if nota1 < 0 or nota1 > 10:
            print('Nota inválida.. O valor deve ser entre 0 e 10')
        else:
            valid_nota=True
    except:
        print('Nota inválida.. Use apenas números e separe os decimais com ponto.(Ex. 9.5)')

valid_nota=False

while valid_nota==False:
    nota2=input('Digite a nota da segunda prova: ')
    try:
        nota2=float(nota2)
        if nota2 < 0 or nota2 > 10:
            print('Nota inválida.. O valor deve ser entre 0 e 10')
        else:
            valid_nota=True
    except:
        print('Nota inválida.. Use apenas números e separe os decimais com ponto.(Ex. 9.5)')

valid_faltas=False

while valid_faltas==False:
    faltas=input('Digite o total de faltas do aluno: ')
    try:
        faltas=int(faltas)
        if faltas < 0 or faltas > 20:
            print('Numero de faltas inválido.. A quantidade de faltas é apenas de 0 a 20')
        else:
            valid_faltas=True
    except:
        print('Preenchimento de faltas inválido.. Use apenas números inteiros')

media=(nota1+nota2)/2
assid=(20-faltas)/20

if media >= 6 and assid >= 0.7:
    resultado='Parabéns, você PASSOU por média e por presença'

elif media <= 6 and assid <= 0.7:
    resultado='Desculpe, mas você reprovou por média e por presença'

elif media >= 6 and assid <= 0.7:
    resultado='Desculpe, mas você reprovou por presença'

elif media <= 6 and assid >= 0.7:
    resultado='Desculpe, mas você reprovou por média'

else:
    print('erro')

print('Aluno:',nome)
print('Média:',media)
print('Assiduidade:',str(assid*100)+'%')
print(resultado)