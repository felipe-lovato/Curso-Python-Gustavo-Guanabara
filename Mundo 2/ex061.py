#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

pa = int(input('Informe PA: '))
razao = int(input('Informe a Razao: '))
cont = 9
print(f'{pa}',end=' > ')
while cont > 0:
    pa += razao
    print(f'{pa}', end=' > ')
    cont -= 1
print('FIM')