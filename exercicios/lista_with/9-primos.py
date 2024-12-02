with open('text.txt','r') as arquivo:
    for linha in arquivo:# verifica número por número do arquivo
        n = int(linha)
        if n <= 1:
            print(f'{n} não é primo')
        elif n == 2:
            print(f'{n} é primo')
        elif n % 2 == 0:
            print(f'{n} não é primo')
        else:
            for i in range(3, int(n ** 0.5) + 1, 2): # Verifica se o n é divizivel até a raiz quadrada dele
                if n % i == 0:
                    print(f'{n} não é primo')
                    break
            else:
                print(f'{n} é primo')