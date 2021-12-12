#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
# os espaços.

frase = str(input('escreva a frase: ').upper())
separa = frase.split()
junta = ''.join(separa)
invertido = ''
for letra in range(len(junta) -1, -1, -1):
    invertido += junta[letra]
print(invertido)
if invertido == junta:
    print('é igual')

