print('Digite 5 números:')
vetor = []
vetor2 = []
produto = []
i = 0
for c in range(1, 6):
    n = int(input(f'{c}º: '))
    vetor.append(n)
print('Digite mais 5 números:')
for c in range(1, 6):
    n = int(input(f'{c}º: '))
    vetor2.append(n)
for c in range(0, 5):
    produto.append(vetor[i] * vetor2[i])# Multiplica os elementos das listas
    i += 1
print(f'Os produtos dos termos das listas são: {produto}')