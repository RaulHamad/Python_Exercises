l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

z = zip(l1,l2)
print(list(z))

lista = [1,2,3,4,5]
tupla = (6,7,8,9,10)
dicionario = {"a": 22, "b": 33, "c": 44, "d": 55, "e": 66}

funcao_zip = list(zip(lista,tupla,dicionario.values()))
print(funcao_zip)

print('-='*30)

v1 = [1200,234,2345,1560]
v2= [1245,300,2103,1434]
p= ['Fogao', 'Liquidificador', 'Geladeira', 'TV']

lista  ={venda[0]: max(venda[1],venda[2]) for venda in zip(p,v1,v2)}
print(lista)