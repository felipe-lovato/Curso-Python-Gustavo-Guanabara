#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.

num = int(input('de qual tabiada deseja? '))
for cont in range(1,10+1):
    print(f"{num} X {cont} = {num*cont}")