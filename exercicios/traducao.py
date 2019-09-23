# Programa traduz uma sequencia de numeros em letras do alfabeto

print('Mensagem secreta')

library = {'0': ' ', '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
           '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r',
           '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'x', '24': 'w', '25': 'y', '26': 'z'}

repetir = True
resultado = []

while repetir == True:

    mensagem = input('Digite um número de 0 á 26: ')

    if mensagem != '':
        procura = library.get(mensagem)

        if procura == None:
            print('Caractere Inválido!. Insira números de 0 á 26 APENAS')
            repetir = True
        else:
            resultado.append(procura)
    else:
        repetir = False

lista = resultado
print(''.join(str(string) for string in lista))
