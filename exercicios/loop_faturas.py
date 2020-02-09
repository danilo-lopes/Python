#### Fatura

fatura=[]
repetir='s'
total=0

while repetir=='s':
    produto=input('Digite o nome do produto: ')
    preco=float(input('Digite o preço do produto: '))
    fatura.append([produto,preco])
    total=(total+preco)
    repetir=input('Deseja comprar mais algum produto? S ou N: ').lower()

for faturas in fatura:
    print(faturas[0],'- R$',faturas[1])

print('O total da fatura é: R$',total)