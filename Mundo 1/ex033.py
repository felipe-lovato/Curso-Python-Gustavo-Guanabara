#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('informe o primeiro numero: '))
num2 = int(input('informe o segundo numero: '))
num3 = int(input('informe o terceiro numero: '))

print(f'O maior numero digitado é {max(num1,num2,num3)}')
print(f'O menor numero digitado é {min(num1,num2,num3)}')