#Faça um prigrama que leia uma frase pelo teclado e mostre
#Quantas veze aparece a letra A
#qual foi a primeira posição que ela apareceu e a ultima

frase = str(input("digite uma frase: ").strip().upper())
print("a letra A apareceu {} na frase ".format(frase.count("A")))
print("a letra a apareceu na primeira vez na posição {} \na letra a apareceu na ultima vez na posição {}".format(frase.find("A"), frase.rfind("A")))