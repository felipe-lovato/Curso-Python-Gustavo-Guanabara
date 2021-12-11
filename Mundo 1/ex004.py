#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('Só espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Esta em maiúsculas? ', a.isupper())
print('Esta em minucula ', a.islower())
print('Esta capitalizada?', a.istitle())