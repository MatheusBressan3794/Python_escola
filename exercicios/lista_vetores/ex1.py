vetor = []
soma = 0
c = 1
print('Digite 10 números:')
for c in range(1, 11):
    n = int(input(f'{c}º nome: '))
    vetor.append(n)
soma = sum(vetor)# Soma todos os números dentro da lista
print(f'Os números arquivados foram: {vetor}')
print(f'A soma de todos eles é {soma}')