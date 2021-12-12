#Faça um programa que leia a largura e a altura de uma parede em meros,
#calcule ea dua area e a quantidade de tinta nescessaria para penta-la, sabendo que cada litro pinta uma area de 2m2

altura=float(input('informe a altura da parede: '))
largura=float(input('informe a largura da parede: '))

print('Area total = {:.2f} \n Quantidade de tinta = {:.3f}L'.format(altura*largura, (altura*largura)/2))