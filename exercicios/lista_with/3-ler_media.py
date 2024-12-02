soma = 0
numero_de_linha = 0
with open('text.txt', 'r') as arquivo:
    for linha in arquivo: # ler linha por linha
        numero_de_linha += 1
        soma += int(linha)
media = soma / numero_de_linha
print(f'A média é: {media}')