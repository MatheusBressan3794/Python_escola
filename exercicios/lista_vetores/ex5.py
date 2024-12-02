print('Digite 5 números')
l1 = []
l2 = []
l3 = []
for c in range(1, 6):
    n = int(input(f'{c}º: '))
    l1.append(n)
print('Digite mais 5 números')
for c in range(1, 6):
    n = int(input(f'{c}º: '))
    l2.append(n)
l3.append(l1 + l2)
print(f'Todos os números juntos: {l3}')