vetor = []
par = 0
print('Digite 15 números')
for c in range(1, 16):
    n = int(input(f'{c}º: '))
    vetor.append(n)
    if n % 2 == 0:
        par += 1
print(f'dos números {vetor}\n{par} são pares')