#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

p_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for cont in range(p_termo,(razao * 10)+p_termo, razao):
    print('{} -> '.format(cont),end='')
print('ACABOU')