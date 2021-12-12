#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de almento.


salario=float(input('Informe o salario: R$ '))
aumento=salario+((salario*15)/100)
print('Seu novo salario é de R$ {:.2f}'.format(aumento))


