#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('=-'*12)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    print('=-' * 12)
    opcao = int(input('escolha uma opção: '))
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'Maior numero: {num1}')
        elif num2 > num1:
            print(f'O maior numero: {num2}')
        else:
            print(f'Os numeros são iguais {num1} e {num2}')
    elif opcao == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando..')
        sleep(2)
    else:
        print('Opção invalida')