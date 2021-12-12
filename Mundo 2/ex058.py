#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0,11)
acertou = False
tentativas = 0
print('Sou seu computador..')
print('Acabei de pensar em um numero de 0 a 10, sera que você consegui adivinhar?')
while not acertou:
    num = int(input('Qual é seu palpite?'))
    tentativas += 1
    if num == computador:
        acertou = True
        print(f'Parabens, vc acertou! Foram {tentativas} tentativas')
    else:
        if num > computador:
            print('- Menos -')
        else:
            print('+ Mais +')
