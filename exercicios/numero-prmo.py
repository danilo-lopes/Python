num = int(input('Digite um número: '))
total=0

for counter in range(1, num+1):
        if num % counter == 0:
            print('\033[33m', end='')
            total+=1
        else:
            print('\033[31m', end='')
        print('{} '.format(counter), end='')

print('\n\033[mO número {} foi divisível {} vezes.'.format(num, total))
    
if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
