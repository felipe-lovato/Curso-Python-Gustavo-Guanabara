#Crie um programa que leia o nome de uma cidade, e diga se ela começa com santo ou não

cidade = str(input("nome da cidade: ")).strip()
print(cidade[:5].upper() == 'SANTO')
