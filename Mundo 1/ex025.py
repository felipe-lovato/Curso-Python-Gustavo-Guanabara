#Crie um provama que leia o nome e diga se tem Silva no nome

nome = str(input("Informe seu nome: ")).strip()
print("Tem Silva no nome? {}". format("SILVA" in nome.upper()))