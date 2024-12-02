m = float(input('Qual é a média necessaria? '))
print('Digite suas notas')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1 + n2 + n3) / 3

print('A média foi {}'.format(media))

if media >= m:
    print('Aluno foi aprovado')

else:
    print('Aluno foi reprovado')