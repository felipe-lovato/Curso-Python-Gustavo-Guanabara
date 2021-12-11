#Escreva um programa que leia um valor em metros e o exiba convertido em centimeteos e milimetros.

medida=float(input('Informe quantos metros: '))
print('Valor convertido para centimetros {:.0f}, milimetros {:.0f}'.format(medida*100, medida*1000))