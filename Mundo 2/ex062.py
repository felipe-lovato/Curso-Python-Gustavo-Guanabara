#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
from time import sleep

pa = int(input('Informe PA: '))
razao = int(input('Informe a Razao: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{pa}', end=' > ')
        pa += razao
        cont += 1
    print('PAUSE')
    mais = int(input('Quanto a mais deseja: '))
