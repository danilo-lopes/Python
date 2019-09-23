# Faça um programa que receba um valor em metros e converta para centimetros e milimetros.

valor = float(input('Digite o valor em metros: '))

km = valor / 1000
hm = valor / 100
decam = valor / 10
dec = valor * 10
cent = valor * 100
mili = valor * 1000

print('A medida em metros corresponde á:\n{:.3f} km\n{} hm\n{:.3f} decam\n{} dec\n{} cent\n{} mili'.format(km,hm,decam,dec,cent,mili))
