lista = []
i = 0
print('Insira 5 itens na lista:')
for c in range(1, 6):
    elemento = input(f'{c}º: ').title()
    lista.append(elemento)

while True:
    pergunta1 = input('Você desejá editar a lista(s/n): ').upper()
    
    if pergunta1 == 'N':
        print('Sua lista ficou:')
        i = 0
        for c in range(1, len(lista) + 1):
            print(f'{c}. {lista[i]}')
            i += 1
        print('Obrigado por usar o programa.')
        break

    elif pergunta1 == 'S':
        pergunta2 = input('Adicionar ou remover elementos(a/r): ').upper()

        if pergunta2 == 'A':
            pergunta3 = int(input('Quantos itens? '))
            for c in range(1, pergunta3 + 1):
                elemento = input(f'{c}º: ').title()
                lista.append(elemento)# Adiciona elemento na lista
                
        elif pergunta2 == 'R':
            pergunta4 = int(input('Número do elemento: '))
            print(f'O item: {lista[pergunta4] - 1}, foi removido')
            del lista[pergunta4 - 1]# Deleta o elemento da posição digitada da lista
    print(f'Sua lista editada foi:')
    i = 0
    for c in range(1, len(lista) + 1):
        print(f'{c}. {lista[i]}')
        i += 1
    if len(lista) == 0:
        print('Todos os elementos foram excluidos')