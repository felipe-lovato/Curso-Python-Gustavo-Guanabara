#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
mediaIdade = 0
idadeHomem = 0
idadeMulher  = 0
HomemVelho = ''
for quant in range(1, 5):
    print(f'---Pessoa {quant}--')
    nome = str(input('Nome: ')).split()
    idade = int(input('Idade: '))
    sexo = int(input('Sexo [1] Masculino \n     [2]Feminino'))
    mediaIdade += idade

    if sexo == 1 and idade > idadeHomem:
        idadeHomem = idade
        homemVelho = nome
    if sexo == 2 and idade < 20:
        idadeMulher += 1

mediaIdade = mediaIdade / 4
print(f'A media de idade é de {mediaIdade}\nO nome mais velho é o {homemVelho} com {idadeHomem}\n tem {idadeMulher} Mulheres com menos de 20 anos')