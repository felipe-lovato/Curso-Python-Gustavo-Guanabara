#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = int(input('Qual a distancia da viagem em KM: '))

if km < 200:
    print(f'O valor da viagem é de {km * 0.50}')
else:
    print(f'O valor da viagem é de {km * 0.45}')