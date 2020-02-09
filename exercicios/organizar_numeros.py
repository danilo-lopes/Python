
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

    number = input('Digite num numero: ')

    for numbers in number:
        numbersList.append(numbers)
        counter += 1

print(shorted(list(numbersList)))
