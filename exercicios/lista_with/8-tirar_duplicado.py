lista_original = []
with open('text.txt','r') as arquivo:
    for linha in arquivo:
        lista_original.append(int(linha))
vetornovo = [] 
totalduplicado = 0
 
for i in lista_original:# Vai número por número do vetor
    if not float(i) in vetornovo:# Se o número não estiver no vetornovo ele adciona
        vetornovo.append(float(i))
    else: 
        totalduplicado += 1
 
print("Lista original: ",lista_original)
print("Lista filtrada: ",vetornovo)

if totalduplicado > 0:
    print(f'{totalduplicado} números duplicados')
elif totalduplicado == 0:
    print('Nenhum número duplicado')