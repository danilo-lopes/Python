# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

userYear = int(input('Digite o ano: '))

if userYear == 0:
    userYear = date.today().year

if userYear % 4 == 0 and userYear % 100 != 0 or userYear % 400 == 0:
    print('O ano {} é bissexto'.format(userYear))
else:
    print('O ano {} não é bissexto'.format(userYear))
