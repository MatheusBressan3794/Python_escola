produto = 1
with open('text.txt', 'r') as arquivo:
    for linha in arquivo:
        produto *= int(linha)
print(f'O produto de todos os números são {produto}')