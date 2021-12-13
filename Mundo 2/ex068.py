# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
while True:
    print('Jogo Impar ou Par')
    escolha = int(input('[1] Impar\n[2] Par\n'))
    op = randint(1, 2)
    print(op)
    if escolha == op:
        print(f'Deu {"IMPAR" if op == 1 else "PAR"} Aee acertou!')
    else:
        print(f'Deu {"IMPAR" if op == 1 else "PAR"} Não foi desse vez')