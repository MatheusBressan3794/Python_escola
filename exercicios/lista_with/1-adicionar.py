for c in range(1,6):
    numero = int(input(f'Digite o {c}º número: '))
    
    with open('text.txt','a') as arquivo:
        arquivo.write(f'{numero}\n')