#Sorteie um dos seus quatros alunos para escrever no quadro.lendo os nomes deles e escrevendo o escolhodo
import random

n1 = str(input('Primeiro Nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('terceiro nome: '))
n4 = str(input('quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O nome escolhido foi {}'.format(escolhido))