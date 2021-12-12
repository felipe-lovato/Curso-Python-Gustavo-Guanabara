#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_hoje = date.today().year
maior = 0
menor = 0

for p in range(1, 9):
    ano = int(input(f'{p} pessoa, informe o ano que voce nasceu:'))
    if ano_hoje - 18 > ano:
        maior += 1
    else:
        menor += 1

print(f'maiores de idade {maior} \nmenores de idade {menor}')