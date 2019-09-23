# Faça um programa que leia algo capturado pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações sobre ele.

word = input('Digite alguma coisa: ')

print('O tipo primitivo do que foi digitado é', type(word))
print('É alfabetico?', word.isalpha())
print('É um valor númerico ?', word.isnumeric())
print('É alfanumerico?', word.isalnum())
print('É só espaços?', word.isspace())
print('Está em maiusculo?', word.isupper())
print('Está em minusculo?', word.islower())
print('Está capitalizada?', word.istitle())
