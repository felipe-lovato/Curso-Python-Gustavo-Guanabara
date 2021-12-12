#leia o nome completo de uma pessoa e motre
#O nome com todas as letras maiusculas
#o nome com todas minusculas
#quantas letras ao tudo sem consideras espaços
#quanstas letras tem o peimeiro nome

nome_completo = str(input("digite seu nome completo: ")).strip()

print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo.replace(" ","")))
print(nome_completo.find(" "))
separa = nome_completo.split()
print(len(separa[0]))