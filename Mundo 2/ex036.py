#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
#valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
#salário ou então o empréstimo será negado.

valorCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salario: '))
anos = int(input('Em quantos anos quer pagar a casa: '))

valorMaximo = salario * 0.30
valorPrestacao = valorCasa / (anos * 12)

if valorMaximo > valorPrestacao:
    print('Seu financiamento foi \33[1;33maprovado\33[m, com prestação de {:.2f}'.format(valorPrestacao))
else:
    print('Seu financiamento foi NEGADO')



print(valorMaximo)
print(valorPrestacao)
