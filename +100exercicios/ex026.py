# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

count = 0
index = 0
allPositions = []

phase = input('Frase: ')
stripPhase = phase.replace(' ', '')


for word in stripPhase:
    if 'a' in word:
        count += 1
        allPositions.append(index + 1)
    index += 1

print('Qtd: {}'.format(count))
print('Fisrt: {}'.format(allPositions[0]))
print('Last: {}'.format(allPositions[:: - 1][0]))
print('Positions: {}'.format(allPositions))
