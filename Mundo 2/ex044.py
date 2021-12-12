#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço do produto: '))

print('Qual a forma de pagamento: ')
print('''[1] - À VISTA DINHEITO/CHEQUE
[2] - À VISTA NO CARTÃO
[3] - 2X NO CARTÃO
[4] - 3X NO CARTÃO''')
escolha = int(input('opção: '))

if escolha == 1:
    valorFinal = preco - (preco * 0.1)
    print('O valor final com desconto é de 10%, Valor: {:.2f}'.format(valorFinal))
elif escolha == 2:
    valorFinal = preco - (preco * 0.05)
    print('O valor final com desconto é de 5% Valor: {:.2f}'.format(valorFinal))
elif escolha == 3:
    print('Em até 2X o valor final é de : {}'.format(preco))
elif escolha == 4:
    valorFinal = (preco * 0.2) + preco
    print('O prelo final com mais 20% ficou de {:.2f}'.format(valorFinal))
else:
    print('A escolha de paramento não corresponde a nenhuma das opçoes')
