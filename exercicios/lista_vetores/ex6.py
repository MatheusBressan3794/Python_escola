print('Digite 10 termos:')
vetor = []
cont = 0
for c in range(1, 11):
    n = float(input(f'{c}º: '))
    vetor.append(n)
    cont += 1
soma = sum(vetor)# Soma todos os elementos da lista/vetor
media = soma / cont
print(f'A média dos números digitados é {media}')