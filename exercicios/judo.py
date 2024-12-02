lu1 = input('Nome do 1º lutador: ')
lu2 = input('Nome do 2º lutador: ')
print('É necessario fazer 10 pontos para ganhar a luta')
print('[ 1 ] IPPON')
print('[ 2 ] WAZA-ARI')
print('[ 3 ] SEGUROU POR 10 SEGUNDOS')
print('[ 4 ] SEGUROU POR 20 SEGUNDOS')
print('[ 5 ] OPONENTE BATEU A MÃO 3 VEZES NO CHÃO')

pontuação1 = 0
pontuação2 = 0

while (pontuação1 > 10) or (pontuação2 > 10):# Vai repetir a pergunta até a pontuação ser igual a 10

    l1 = int(input('Qual golpe foi aplicado pelo 1º lutador? '))
    l2 = int(input('Qual golpe foi aplicado pelo 2º lutador? '))

    if (l1 or l2 == 1):
        print('10 PONTOS')
        if l1 == 1:
            pontuação1 += 10
        elif l2 == 1:
            pontuação2 += 10

    elif (l1 or l2 == 2):
        print('5 PONTOS')
        if l1 == 2:
            if pontuação1 == 0:
                print('\n O 1º lutador precisa de mais 5 pontos para ganhar a luta')
            pontuação1 += 5
    elif l2 == 2:
        if pontuação2 == 0:
            print('\n O 2º lutador precisa de mais 5 pontos para ganhar a luta')
            pontuação2 += 5

    elif (l1 or l2 == 3):
        print('5 PONTOS')
        if l1 == 3:
            if pontuação1 == 0:
                print('\n O 1º lutador precisa de mais 5 pontos para ganhar a luta')
            pontuação1 += 5
        elif l2 == 3:
            if pontuação2 == 0:
                print('\n O lutador precisa de mais 5 pontos para ganhar a luta')
            pontuação2 += 5

    elif (l1 or l2 == 4):
        print('10 PONTOS')
        if l1 == 4:
            pontuação1 += 10
        elif l2 == 4:
            pontuação2 += 10

    elif (l1 or l2 == 5):
        print('10 PONTOS')
        if l1 == 5:
            pontuação1 += 10
        elif l2 == 5:
            pontuação2 +=  10
if pontuação1 >= 10:
    print('O {} GANHOU a luta, parabéns!'.format(lu1))
elif pontuação2 >= 10:
    print('O {} GANHOU a luta, Parabéns!')