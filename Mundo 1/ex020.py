#sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia nomes e mosrew a ordem
from random import shuffle
n1 = str(input('Primeiro Aluno'))
n2 = str(input('segundo Aluno'))
n3 = str(input('terceiro Aluno'))
n4 = str(input('quarto aluno'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
 
