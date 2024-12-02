nomes = []
idades = []
parar = int(input('Quantas pessoas serão registradas? '))
p = 0
while p != parar:
    nome = input('Digite o nome: ').capitalize()
    nomes.append(nome)# Acrecenta o nome digitado na lista nomes

    idade = int(input('Qual a sua idade? '))
    idades.append(idade)# Acrecenta a idade digitada na lista idades
    p += 1
print(nomes)
print(idades)