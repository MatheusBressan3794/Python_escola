print('Digite 10 números:')
vetor = []
repetido = 0
for c in range(1, 11):
    n = int(input(f'{c}º: '))
    if n in vetor:# se n estiver no vetor
        repetido += 1
    else:
        vetor.append(n)
print(f'Os números armazenados foram: {vetor}')
print(f'Você repetiu números {repetido} vezes')