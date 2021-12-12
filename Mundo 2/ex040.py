#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

nota1 = float(input('informe a primeira nota: '))
nota2 = float(input('informe a segunda nota: '))
media = (nota1 + nota2) / 2
print('A media é de {:.1f}'.format(media))

if media >= 7:
    print('Parabens, Passou')
elif media < 7 and media >= 5:
    print('Esta em recuperacao')
else:
    print('Reprovado')