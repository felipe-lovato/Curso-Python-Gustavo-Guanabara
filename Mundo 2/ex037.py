#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('informe um numero inteiro: '))
print('*' * 12)
print('DESEJA CONVERTER PARA:')
print('[1] - BINÁRIO')
print('[2] - OCTAL')
print('[3] - HEXADECIMAL')
escolha = int(input('-- '))

if escolha == 1:
    print(f'Binario: {bin(num)[2:]}')

elif escolha == 2:
    print(f'Octal: {oct(num)[2:]}')

elif escolha == 3:
    print(f'Hexadecimal: {hex(num)[2:]}')

else:
    print('nenhuma escolha foi selecionada corretamente!')