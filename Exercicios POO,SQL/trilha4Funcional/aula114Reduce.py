from functools import reduce
lista = [1,2,3,4,5,6,7,8,9,10]

r = reduce(lambda x,y : x+y, lista)
print(r)

print('-='*30)
#somar todas as idades das pessoas menores de idade
pessoas = [
    {"nome": 'Joao', "idade": 12},
    {"nome": 'carla', "idade": 34},
    {"nome": 'jose', "idade": 16},
    {"nome": 'adriana', "idade": 6},
    {"nome": 'ronny', "idade": 90}
]

idades = list((map(lambda x : x['idade'],pessoas)))
print(idades)
idade_menores = list(filter(lambda x : x<18, idades))
print(idade_menores)
somar_idades_menores = reduce(lambda x,y:x+y,idade_menores)
print(somar_idades_menores)