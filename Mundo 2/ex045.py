#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')

while True:
    print('''Jogo Jokenpô
        [0] Pedra
        [1] Papel
        [2] Tesoura''')

    escolha = int(input('Opção: '))
    escolhaPc = randint(0, 2)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ !!')
    sleep(0.5)

    print('-=' *15)
    print(f'Computador jogou {itens[escolhaPc]}')
    if 0 <= escolha <= 2:
        print(f'{itens[escolha]} e {itens[escolhaPc]}')
    if escolha == 0:
        if escolhaPc == 0:
            print('Empate!')
        elif escolhaPc == 1:
            print('O Computador ganhou :(')
        else:
            print('Você Ganhou, Parabens!!')
    elif escolha == 1:
        if escolhaPc == 0:
            print('Você Ganhou, Parabens!!')
        elif escolhaPc == 1:
            print('Empate!')
        else:
            print('O Computador ganhou :(')
    elif escolha == 2:
        if escolhaPc == 0:
            print('O Computador ganhou :(')
        elif escolhaPc == 1:
            print('Você Ganhou, Parabens!!')
        else:
            print('Empate!')
    else:
        print('Opção invalida')
    print('-=' *15)

