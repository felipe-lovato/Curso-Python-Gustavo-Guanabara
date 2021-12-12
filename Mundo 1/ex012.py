#Faça um algoritimo que leia o prelo de um produto e mostre seu novo preço, com 5¢ de desconto

preco = float(input('Valor do produto: R$ '))
desconto = preco - ((preco*5)/100)
print('Novo preço com 5% de desconto R$ {:.2f}'.format(desconto))