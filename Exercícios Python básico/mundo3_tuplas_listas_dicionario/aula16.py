# LISTAS

lanche = ['hamburguer', 'suco', 'pizza', 'pudin', 'ovo', 'pao', 'frango']
print(lanche)
lanche[3] = 'picole' # Nas listas podemos alterar os itens
print(lanche)

lanche.append('cerveja') # adiciona item no ultimo indice da lista
print(lanche)
lanche.insert(2,'cafe') # inseri item no indice escolhido 
print(lanche)

del lanche[3] #remove da lista o indice escolhido
print(lanche)
lanche.pop() #remove o ultimo indice da lista ou pode ser
# escolhido tbm EX: (3)
print(lanche)
lanche.remove('suco') # remove da lista o indice DIGITADO
print(lanche)


if 'ovo' in lanche:
    lanche.remove('ovo')
print(lanche)


valores = [8,2,5,4,9,3,0]
valores.sort()
print(valores)
valores.sort(reverse=True) # coloca em ordem decrescente
print(valores)
print(len(valores))

lista1 = list()
for cont in range(0,5):
    lista1.append(input('Digite um valor: '))
for c, v in enumerate(lista1):
    print(f'Na posição {c} tem o valor {v}')

d = [2, 4, 6, 8]
f = d # python cria uma ligação que se alterar F ira alterar D tambem
f[2] = 7
print(d)
print(f)

g = [1, 2, 3, 4]
f = g[:] # f cria uma copia de g que pode se alterada sem mexer no g
f[0] = 9
print(f)