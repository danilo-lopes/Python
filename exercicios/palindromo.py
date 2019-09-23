# faça um código que leia uma frase e mostre se ela é um palíndromo ou não

phrase = str(input('Digite uma frase: ').replace(' ', '').upper())

if phrase == phrase[::-1]:
    print('{} é um palindromo. Pois {} invertido é {} '.format(phrase.upper(), phrase.upper(), phrase[::-1].upper()))
else:
    print('{} não é um palindromo. Pois {} invertido é {}'.format(phrase.upper(), phrase.upper(), phrase[::-1].upper()))
