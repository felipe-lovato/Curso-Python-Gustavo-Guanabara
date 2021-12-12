#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.
continua = True
minimo = maximo = media = 0
cont = 1
while continua:
    num = int(input('Digite um valor: '))
    if cont == 1:
        maximo = minimo = num
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num
    media += num
    cont += 1
    valida = ''
    while valida != 'N' and valida != 'S':
        valida = input('Deseja continuar [S] [N] : ').upper().split()[0]
        if valida == 'N':
            continua = False
print(f'Media = {media/cont:.1f}')
print(f'Maior Valor {maximo}\nMenor valor {minimo}')