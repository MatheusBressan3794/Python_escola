print('Digite 10 números:')
vetor = []
maior = menor = 0
c = 1
for c in range(1, 11):
    n = int(input(f'{c}º: '))
    vetor.append(n)
    if c == 1:# O primeiro número digitado vai ser o maior e menor
        maior = n
        menor = n
    else: # nos demais ele vai verificar
        if n > maior:# Se o número for maior que o maior, ele passa a ser o maior
            maior = n
        if n < menor:# Se o número for menor que o menor, ele passa a ser o menor
            menor = n
print(f'Os números armazenados foram {vetor}')
print(f'O maior número foi {maior} e o menor foi {menor}')