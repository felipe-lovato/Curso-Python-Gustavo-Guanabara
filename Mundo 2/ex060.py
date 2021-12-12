#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

fat = int(input('Qual numero deseja calcular o seu fatorial: '))
mult = 1
while fat > 0:
    mult *= fat
    print(fat, end= ' ')
    print('X'if fat > 1 else '=', end= ' ')
    fat -= 1
print(f'{mult}')