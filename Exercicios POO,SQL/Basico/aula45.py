lista = []
lista2 = []
while True:
    c = input('Digite uma palavra: ')
    
    if c == '':
        break
    lista.append(c)
print(lista)
    
for c in lista:
    lista2.append(list(set(c)))
    print(lista2)

for c in lista2:
    print(c)
###############
produtos = [
    'nome', "preco",'toto','banana'
    
]

lista = []
for c in produtos:
    lista.append((set(c)))

for k in lista:
    print(k)

    
