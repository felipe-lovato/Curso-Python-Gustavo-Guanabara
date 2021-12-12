#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Qual numero deseja verificar se é primo: '))
soma = 0
for cont in range(1, num+1):
    if num % cont == 0:
        print(f'\33[32m{cont}\33[m', end=' ')
        soma += 1
    else:
        print(f'\33[31m{cont}\33[m', end=' ')
print('\n')
if soma < 3:
    print('O numero {} é PRIMO'.format(num))
else:
    print(f'O numero {num} não é primo')