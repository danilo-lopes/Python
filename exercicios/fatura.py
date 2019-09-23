# -*- coding: utf-8 -*-
##Crie um código que faça o usuário digitar o nome do produto, preço e ao final exibir o
##total da fatura dele. A cada produto e preço pergunte a ele se deseja adicionar mais algum
##produto.

repetir='s'
fatura=[]
total=0
valid_preco=False

while repetir=='s':
    produto=input('Digite o nome do produto: ')

    while valid_preco==False:
        preco=(input('Digite o preco do produto: '))
        try:
            preco=float(preco)   
            if preco < 0:
                print('O preço precisa ser maior do que zero')
            else:
                valid_preco=True
        
        except:
               print("Formato de número inválido. Use apenas números e separe os centavos com '.'") 
           
    fatura.append([produto,preco])    
    total+=preco   
    valid_preco=False  
    repetir=input('Deseja comprar mais algum produto? "S ou N": ').lower() 
    
for result in fatura:   
    print(result[0],'-',result[1])  
                                    
print('O total da sua fatura é:',total) 
input('Digite ENTER para sair')