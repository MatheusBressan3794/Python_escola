comidas = ['Pastel', 'Cachorro Quente', 'Cuscuz', 'Lanche Caipira', 'Milho Cozido', 'Pipoca', 'Espetinho de Carne', 'Refrigerante', 'Água', 'Água com Gás', 'Bolo de Pote', 'Bolo Bombom', 'Coxinha de Morango', 'Cone', 'Cocada', 'Espeto de morango', 'Caixa com 4 Brigadeiros', 'Bolacha', 'Brigadeiro Individual', 'Trufas']
preços = [4.00, 10.00, 10.00, 15.00, 8.00, 2.00, 10.00, 6.00, 3.00, 5.00, 12.00, 9.00, 9.00, 9.00, 9.00, 12.00, 12.00, 12.00, 4.00, 6.00]
fichas_total = [0] * len(comidas)
valor_total = [0] * len(comidas)
numero_clientes = produtos =  total = 0

print('Bem-vindo(a) á festa primavera da FATEC Araras')
print('CARDAPIO:')
for c in range(0, 19):# Mostra o cardápio baseado nas pasições do vetor
    print(f'[ {c + 1} ]  {comidas[c]}: R${preços[c]}')

while True:# Registra o nome do cliente
    cliente = input('Nome do cliente: ').title()
    numero_clientes += 1
    itens = []# Itens pegos por cada cliente
    valor_gasto = []# Valor gasto pelo cliente em cada produto
    fichas_cliente = []# Fichas de cada cliente
  
    while True:# Registra o pedido do cliente
        pedido = int(input('Qual pedido (digite 0 para encerrar o pedido): '))

        if 1 <= pedido and pedido <= len(comidas):# Se o pedido for maior igual a 1 e menor igual a len(comidas) que é = 20 
            i = pedido - 1 # para o pedido ser o mesmo da posição do vetor
            n = int(input(f'Quantos {comidas[i]}: '))

            produtos += 1
            itens.append(comidas[i])# Acrescenta a comida comprada
            valor_gasto.append(n * preços[i])# Vai acrescentar o valor gasto em cada comida por cliente
            valor_total[i] += n * preços[i]# Preço gasto em cada comida no total
            fichas_cliente.append(n)# Quantia de fichas no total
            total += n * preços[i]# Valor total
            fichas_total[i] += n # Fichas do cliente

        elif pedido == 0:# Pedido 0 encerra
            print(f'\nO pedido do cliente {cliente} foi:')

            for c in range(0, len(itens)):
                print(f'{fichas_cliente[c]} ficha(s) de {itens[c]} = R${valor_gasto[c]}')

            print(f'Total de R${sum(valor_gasto)}\n')# Soma os valores do vetor: valor_gasto
            break

        else:
            print('Essa opção não existe no cardápio')

    r = input('Fechar o caixa(s/n)? ').upper()
    if r == 'S':
        break
    
print(f'\nForam atendidos {numero_clientes} clientes;')
print(f'{produtos} itens vendidos;')
print(f'O total de dinheiro arrecadado foi de R${total}.\n')
print('Foram vendidas:')
for c in range(1, len(comidas)):
    print(f'{fichas_total[c]} de {comidas[c]} = {valor_total[c]}')