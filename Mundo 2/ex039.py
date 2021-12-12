#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nascimento = int(input('informe o ano de nascimento: '))
ano = date.today().year - nascimento

if ano > 18:
    print(f'Ja passou do tempo de se alistar a {ano-18} anos, seu alistamento foi em {date.today().year - (ano-18)}')
elif ano < 18:
    print(f'faltam {18-ano} anos para se alistar, sera no ano de {date.today().year + (18-ano)}')
else:
    print('esta na hora de se alistar')
