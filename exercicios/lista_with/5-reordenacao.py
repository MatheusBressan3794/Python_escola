vetor = []
with open('text.txt','r') as arquivo:
    for linha in arquivo:
        vetor.append(int(linha))
        crescente = sorted(vetor)
        decrescente = sorted(vetor, reverse = True)

print('Lista em ordem crescente: ')
print(crescente)
print('Lista em ordem decrescente: ')
print(decrescente)