#Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
#coding: utf-8
from time import sleep
num = int(input('Escolha um numero: '))
for cont in range(num, -1, -1):
    print(cont)
    sleep(1)