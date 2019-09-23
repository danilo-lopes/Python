
x=0
pessoas=[]

while x < 4:
    nome=input('Qual o seu nome?: ')
    if nome == 'joao':
        break
    pessoas.append(nome)
    x+=1
     
print(pessoas)
