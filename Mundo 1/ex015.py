#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

x = float(input('Quantos kilometros foi andado com o carro?'))* 0.15
y = int(input('Quantos dias ele foi usado?'))* 60
print(f'Então será cobrado {x + y :.2f} reais .')