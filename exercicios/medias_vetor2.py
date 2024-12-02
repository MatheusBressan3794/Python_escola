n_alunos = int(input('Quantos alunos? '))
# Vetores vazios
nomes = []
prova1 = []
prova2 = []
medias = []

# Vai adicionar os nomes e a medias nos vetores
for c in range(1, n_alunos + 1): 
    nome = input('Qual o nome do {}º aluno: '.format(c)).title()
    nomes.append(nome)# Adiciona o nome digitado na lista de nomes

    n1 = float(input('Nota da 1º prova: '))
    prova1.append(n1)
    n2 = float(input('Nota da 2º prova: \n'))
    prova2.append(n2)
    
    media = (n1 + n2) / 2# Calcula a média de cada aluno
    medias.append(media) # Adiciona a média na lista medias

# i = 0 e vai almentando de 1 em 1 
for i in range(n_alunos):# 
    # Verifica se o aluno foi aprovado ou reprovado
    if medias[i] >= 7:
        comentario = 'APROVADO'
    else:
        comentario = 'REPROVADO'

    print('Aluno {} está {}'.format(nomes[i], comentario))# Nomes[i] vai ser = ao primeiro nome digitado, depois o segundo...
    print('Prova 1 = {}'.format(prova1[i]))# prova1[i] vai ser = ao primeira nota digitada, depois a segunda...
    print('Prova 2 = {}'.format(prova2[i]))# prova2[i] vai ser = ao primeira nota digitada, depois a segunda...
    print('Sua média foi de {}\n'.format(medias[i]))# Média[i] também vai ser a primeira calculada, depois a segunda...