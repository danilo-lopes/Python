# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


def shorted(numbersList):
    left = []
    middle = []
    right = []

    if len(numbersList) > 1:
        location = numbersList[0]

        for number in numbersList:
            if number < location:
                left.append(number)
            if number == location:
                middle.append(number)
            if number > location:
                right.append(number)

        return shorted(left) + sorted(middle) + sorted(right)

    else:
        return numbersList


qtd = int(input('Quantos numeros deseja organizar?: '))
counter = 0
numbersList = []

while qtd > counter:

    number = input('Digite: ')

    for numbers in number:
        numbersList.append(numbers)
        counter += 1


print(shorted(list(numbersList)))

organizedNumbers = sorted(list(numbersList))

lessNumber = organizedNumbers[0]
biggerNumber = organizedNumbers[:: -1][0]

print('O menor número da lista é o {}'.format(lessNumber))
print('O maior número da lista é o {}'.format(biggerNumber))



# firstNumber = int(input('Digite o primeiro número: '))
# secoundNumber = int(input('Digite o primeiro número: '))
# thirtyNumber = int(input('Digite o primeiro número: '))
#
# listNumber = [firstNumber, secoundNumber, thirtyNumber]
#
# sortedNumbers = sorted(listNumber)
#
# print('Menor número: {}'.format(sortedNumbers[0]))
# print('Maior número: {}'.format(sortedNumbers[:: -1][0]))
