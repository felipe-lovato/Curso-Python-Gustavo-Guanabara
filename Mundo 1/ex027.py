#Leio um nome e apresente o nome e seu sobrenome

n = str(input('Digite seu nome e sobrenome: ')).strip().upper()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu sobrenome é {}'.format(nome[len(nome)-1]))