#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date

print('*--*' *10)
print('Confederação Nacional de Natação')
print('*--*' *10)

nasc = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - nasc
print ('Sua idade é {}'.format(idade))

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif 10 < idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')