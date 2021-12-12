#Crie um programa que leia um numero real e mostre na tela a sua porção inteira
from math import trunc

num = float(input('Digite um numero: '))
print('o seu numero inteiro é {:.0f}'.format(num))
print('o numero com floor {}'.format(trunc(num)))