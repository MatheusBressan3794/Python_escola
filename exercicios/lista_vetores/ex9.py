print('Digite 10 números:')
vetor = []
for c in range(1, 11):
    n = int(input(f'{c}º: '))
    vetor.append(n)
vetor_ordenado = sorted(vetor)# Coloca o vetor em ordem crescente
print(vetor_ordenado)