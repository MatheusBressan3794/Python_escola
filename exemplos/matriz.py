num_alu = int(input('Digite o número de alunos: '))
num_mat = int(input('Digite o número de matérias: '))

matriz = [[0] * num_mat for _ in range(num_alu)]

for i in range(num_alu):
    print(f'Digite as notas do Aluno {i + 1}:')
    for j in range(num_mat):
        matriz[i][j] = float(input(f'Nota{j + 1}: '))

print('/nMédia dos alunos:')

for i in range(num_alu):
    soma = 0
    for j in range(num_mat):
        soma += matriz[i][j]
    media = soma / num_mat
    print(f'Média do aluno {i+1}: {media}')