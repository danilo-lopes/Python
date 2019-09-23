# Faça um programa que receba uma data "20-03-2019" e escreva ela por extenso
# Hoje é dia vinte de março de dois mil e dezenove.

user = input('Digite a data: ').split('/')

indiceDay = {'1': 'primeiro', '2': 'dois', '3': 'tres', '4': 'quatro', '5': 'cinco', '6': 'seis', '7': 'sete',
             '8': 'oito', '9': 'nove', '10': 'dez', '11': 'onze', '12': 'doze', '13': 'treze', '14': 'quatorze', '15': 'quize',
             '16': 'dezeseis', '17': 'dezesete', '18': 'dezoito', '19': 'dezenove', '20': 'vinte', '21': 'vinte e um',
             '22': 'vinte e dois', '23': 'vinte e trez', '24': 'vinte e quatro', '25': 'vinte e cinco',
             '26': 'vinte e seis', '27': 'vinte e sete', '28': 'vinte e oito', '29': 'vinte e nove', '30': 'trinta',
             '31': 'trinta e um'}

indiceMonth = {'1': 'janeiro', '2': 'fevereiro', '3': 'março', '4': 'abril', '5': 'maio', '6': 'junho', '7': 'julho',
               '8': 'agosto', '9': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}

milhar = {'0': '', '1': 'mil ', '2': 'dois mil ', '3': 'tres mil ', '4': 'quatro mil ', '5': 'cinco mil ',
          '6': 'seis mil ', '7': 'sete mil ', '8': 'oito mil ', '9': 'nove mil '}

centena = {'0': '', '1': 'cento e ', '2': 'duzentos e ', '3': 'trezentos e ', '4': 'quatrocentos e ',
           '5': 'quinhentos e ', '6': 'seiscentos e ', '7': 'setescentos e ', '8': 'oitocentos e ',
           '9': 'novecentos e '}

dezena = {'0': '', '1': 'dez ', '2': 'vinte e ', '3': 'trinta e ', '4': 'quarenta e ', '5': 'cinquenta e ',
          '6': 'sesenta e ', '7': 'setenta e ', '8': 'oitenta e ', '9': 'noventa e '}

unidade = {'0': '', '1': 'um', '2': 'dois', '3': 'trez', '4': 'quatro', '5': 'cinco',
           '6': 'seis', '7': 'sete', '8': 'oito', '9': 'nove'}


findUserDay = user[0]
findUserMonth = user[1]
findUserYear = user[2]
numberYear = findUserYear

resultMilhar = str(numberYear)[0]
#print(resultMilhar)

resultCenteza = str(numberYear)[1]
#print(resultCenteza)

resultDezena = str(numberYear)[2]
#print(resultCenteza)

resultUnidade = str(numberYear)[3]
#print(resultUnidade)


userDay = indiceDay.get(findUserDay)
userMonth = indiceMonth.get(findUserMonth)

if resultMilhar in milhar:
    getMilhar = milhar.get(resultMilhar)

if resultCenteza in centena:
    getCentena = centena.get(resultCenteza)

if resultDezena in dezena:
    getDezena = dezena.get(resultDezena)

if resultUnidade in unidade:
    getUnidade = unidade.get(resultUnidade)

resultYear = (getMilhar+getCentena+getDezena+getUnidade)

print('{} de {} de {}'.format(userDay, userMonth, resultYear))
