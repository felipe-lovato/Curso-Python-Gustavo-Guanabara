# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
homem = 0
mulher = 0
maior = 0
while True:
    print('-'*23,'\n---- NOVO CADASTRO ----')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper().split()[0]
    if sexo == 'M':
        homem += 1
    elif idade < 20:
        mulher += 1
    if idade > 18:
        maior += 1
    repetir = input('Quer continuar? [S/N]').upper()
    if repetir == 'N':
        print('Finalizando..')
        break
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {homem} homem cadastrados.')
print(f'E tamos {mulher} mulher com menos de 20 anos.')