import math

def area_cirulo(x):
    return math.pi*(x*x)

raios= [3.4,5,2.4,11.3,1.5]

areas = list(map(area_cirulo,raios))
print((areas))
#--------------------------------------
areas2 = list(map(lambda x: math.pi*(x**2), raios))
print(areas2)

produtos = [('tv', 2500), ('fogao', 1240), ('radio', 234)]

novo_preco = lambda x : (x[0], x[1] * 1.05)

print(list(map(novo_preco, produtos)))
# ----------------------------------------
lista = [
    {"nome": 'Jose', "idade": 28},
    {"nome": 'Adriana', "idade": 39},
    {"nome": 'Pedro', "idade": 50},
    {"nome": 'Maria', "idade": 23}
]

so_nomes = list(map(lambda x : x["nome"], lista))
print(so_nomes)
so_idades = list(map(lambda idade: idade["idade"], lista))
print(so_idades)
soma_das_idades = sum(so_idades)
print(soma_das_idades)

print(sorted(lista, key=lambda x : x['nome'],reverse=False))

print(lista)