#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep

numero = randrange(0, 6)
print( '--=' *8)
adivinha = int(input('Adivinha qual o numero: '))
print( '--=' *8)
print('PENSANDO...')
sleep(1)

if numero == adivinha:
    print('PARABENS, VC ADIVINHOU O NUMERO')
else:
    print(f'o Computadot ganhou, o numero era {numero}')