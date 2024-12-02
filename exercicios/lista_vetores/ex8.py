print('Digite 5 números:')
vetor = []
for c in range(1, 6):
    n = int(input(f'{c}º: '))
    vetor.append(n)
novo_vetor = vetor[-1:] + vetor[:-1]# Move o elemento 1 casa para a direita
print(novo_vetor)
'''A expressão vetor[-1:] fornece uma lista com o último elemento da lista original.
A expressão vetor[:-1] fornece uma lista com todos os elementos da lista original, exceto o último.O operador + é usado para concatenar duas listas'''