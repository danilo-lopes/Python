idade=int(input('Digite a sua idade: '))
sexo=input('Digite o sexo M ou F: ').lower()
cidade=input('Digite a cidade: ').lower()

if cidade=='rio' or cidade=='sao paulo':

    if sexo=='m':
        if idade < 18:
            print('Homem menor de idade, da regiao sudeste')
        else:
            print('Homem maior de idade, da regiao sudeste')

    elif sexo=='f':
        if idade < 18:
            print('Mulher menor de idade, da regiao sudeste')
        else:
            print('Mulher maior de idade, da regiao sudeste')

    else:
        print('Erro na entrada de dados')
else:
    print('teste apenas a região sudeste')