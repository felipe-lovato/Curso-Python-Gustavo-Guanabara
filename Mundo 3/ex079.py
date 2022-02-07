# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
valida = ''
numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num in numeros:
        print(f'O numero {num} ja existe na lista, não vou adicionar')
    else:
        numeros.append(num)
        print(f'O numero {num} foi adicionado com sucesso.')
    while valida != 'S' and valida != 'N':
        valida = input('deseja continuar? [S/N]').upper()
    if valida == 'S':
        valida = ''
    else:
        print('*-*' *20)
        print(numeros )
        break