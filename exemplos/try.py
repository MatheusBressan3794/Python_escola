try: # Código que pode gerar uma exceção
    with open("text.txt","r") as arquivo:
        conteudo = arquivo.read()# Vai ler o arquivo
        print('Conteúdo do arquivo:')
        print(conteudo)
except FileNotFoundError:# Caso der esse erro(exceção)
    print('O arquivo não foi encontrado')