nome=input('Digite o seu nome: ')
nota_prova1=float(input('Digite a sua nota da prova 1: '))
nota_prova2=float(input('Digite a sua nota da prova 2: '))
total_faltas=int(input('Digite o seu total de faltas: '))

media=(nota_prova1+nota_prova2)/2
assid=float(20-total_faltas)/20

if media >= 6 and assid >= 0.7:
    resultado = 'APROVADO'

elif media < 6 and assid < 0.7:
    resultado = 'REPROVADO por média e por presença'

elif media < 6:
    resultado = 'REPROVADO por média'

elif assid < 0.7:
    resultado = 'REPROVADO por presença'

else:
    print('Erro')


print('Nome:', nome)
print('Média:', media)
print('Presença:',str(assid*100)+'%')
print('Resultado:',resultado)
print=input('Digite ENTER para sair')
