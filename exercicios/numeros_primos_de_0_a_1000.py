# Mostrar os números primos de 0 á 1000

count = 0

for num1 in range(1, 1001):
    if num1 > 1:
        for num2 in range(2, num1):
            if num1 % num2 == 0:
                break
        else:
            print('Número Primo', num1)
            count += 1
print('Existem:', count, 'numeros primos de 0 á 1000')
