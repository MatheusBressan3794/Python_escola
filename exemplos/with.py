nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
telefone = input('Digite seu telefone: ')

with open("contatos.txt", "a") as arquivo: # AS para dar nome 
    arquivo.write(f'{nome} - {email} - {telefone}\n')
    
print("Dados escritos em 'contatos.txt'")
'''
r = leitura
w = escrita. Substitui o conteúdo existente
x = escrita. Retorna um erro caso o arquivo já exista
a = escrita. Insere novos dados no final do arquivo
b = modo binário
t = modo de texto(padrão)
+ = Atualizar. Tanto leitura quanto escrita
'''