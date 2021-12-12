#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('informe um numero: '))
resto = (numero % 2) == 0

if resto:
    print(f'O numero {numero} é PAR')
else:
    print(f'O numero {numero} é IMPAR')