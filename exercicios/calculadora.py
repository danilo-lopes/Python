num1 = int(input('Tabuada do número: '))
num2 = int(input('Quantidade de vezes: '))

for count in range(num2):
    print('{} x {} = {}'.format(num1, count, num1*count))