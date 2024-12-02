with open('text.txt','r') as arquivo:
    for linha in arquivo:
        n = int(linha)
        fatorial = n
        print(f'{n} ', end='')
        if n > 0:
            for i in range(n - 1, 0, -1):
                fatorial *= i
                print(f'x {i} ', end='')
            print(f'= {fatorial}')