print('Digite 10 números')
vetor = []
for c in range(1, 11):
    n = int(input(f'{c}º: '))
    vetor.append(n)
print(f'Lista original: {vetor}')
vetor.reverse()# Inverte os elementos da lista
print(f'Lista reversa:  {vetor}')