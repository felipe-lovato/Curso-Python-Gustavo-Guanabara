# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

while True:
    soma = 0
    cont = 0
    menor_p = 0
    pbarato = ''

    print('-'*20,'\n-----SUPER LOJA-----')
    produto = input('Nome do produto: ')
    preco = float(input('Preço: '))
    soma += preco
    if menor_p == 0:
        menor_p = preco
        pbarato = produto
    elif preco < menor_p:
        menor_p = preco
        pbarato = produto

    if preco > 1000:
        cont += 1
    contin = input('Quer continuar?  [S/N]').upper()
    if contin == 'N':
        print('Finalizando..')
        print('-'*7,'FIM DO PROGRAMA','-'*7)
        break
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi o {pbarato} custando {menor_p:.2f}')