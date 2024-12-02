alunos = ['Matheus','Miguel','Nicolas','Pedro','Ruan']# Nome dos alunos
notas_p1 = [10, 7, 5, 3, 8]# Notas da prova 1
notas_p2 = [10, 9, 7, 8, 9]# Notas da prova 2

print('Alunos: ',alunos)
print('Notas da p1: ',notas_p1)
print('Notas da p2: ',notas_p2)

medias = [0, 0, 0, 0, 0]# Ele não permite um vetor vazio, então tem que criar valendo 0
i = 0
while i <= 4:
    medias[i] = ((notas_p1[i] + notas_p2[i]) / 2)
    i += 1
i = 0
while i <= 4:
    print('Aluno: {}'.format(alunos[i]))
    print('1º Prova: {}'.format(notas_p1[i]))
    print('2º Prova: {}'.format(notas_p2[i]))
    print('Sua nota média: {}'.format(medias[i]))
    i += 1