#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for c in range(0,5):
    numeros.append(int(input('Digite um valor: ')))
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros[c] > mai:
            mai = numeros[c]
        if numeros[c] < men:
            men = numeros[c]

print(numeros)
print(f'o maior numero é {mai} na posição ')
for i, v in enumerate(numeros):
    if v == mai:
        print(f'{mai}...')
print(f'o menor numero é {men} na posição ')
for i, v in enumerate(numeros):
    if v == men:
        print(f'{men}...')