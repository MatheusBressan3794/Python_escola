with open('text.txt','r') as arquivo:
    leitura = arquivo.readlines()
    maior = max(leitura)
    menor = min(leitura)
    
print(f'O maior número da lista é: {maior}')
print(f'O menor número é: {menor}')