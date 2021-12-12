#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja
# errado, peça a digitação novamente até ter um valor correto.
while True:
    Sexo = str(input('Sexo [M/F]: ')).upper()
    while Sexo != 'M' and Sexo != 'F':
        print('--Atenção-- Digite [M/F] ')
        Sexo = str(input('Sexo [M/F]: ')).upper()

        