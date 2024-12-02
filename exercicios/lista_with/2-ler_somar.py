total = 0
with open('text.txt','r') as arquivo:
    for linha in arquivo:
        total += int(linha)

print(f'A soma dos números é: {total}')