# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
ponto = 0
while True:
    numero = int(input('Digite um valor :'))
    opcao = input('Par ou Impar [P/I]').upper()
    op = randint(1, 100)
    resul = 'P' if op % 2 == 0 else 'I'
    if resul == op:
        print(f'Você Venceu, Numero:{op+numero} - {"PAR" if (op+numero) % 2 == 0 else "IMPAR"}')
        ponto += 1
    else:
        print(f'Você Perdeu, Numero:{op + numero} - {"PAR" if (op + numero) % 2 == 0 else "IMPAR"}')
        break
print(f'Total de vitoria = {ponto}')
print('Finalizando..')
