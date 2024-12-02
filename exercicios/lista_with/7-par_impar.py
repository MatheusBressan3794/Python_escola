par = []
impar = [] 
with open('text.txt','r') as arquivo:
    for linha in arquivo:
        if int(linha) % 2 == 0:
            par.append(linha.strip())
        elif int(linha) % 2 == 1:
            impar.append(linha.strip())
print(f'Os números pares são: {par}')
print(f'Os impares são {impar}')