#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('informe o seu salario: '))
if salario >= 1250.00:
    print(f'Seu novo salario é de {(salario * 0.10)+salario}')
else:
        print(f'Seu novo salario é de {(salario * 0.15) + salario}')