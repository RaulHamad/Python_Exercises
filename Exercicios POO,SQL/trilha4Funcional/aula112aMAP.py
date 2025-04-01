lista = [1,2,3,-4,5]
a= (map(abs, lista))#uma vez que consome os dados ele nao existe mais, 
#por isso salvar em uma variavel
#print(a) so consome uma vez
#print(a)
l = list(a)
print(l)
b = list(map(str, lista))
print(b)
print(b)

c = list(map(lambda x : x*x*x, lista))
print(c)

lista2 = [11,12,13,14,15]
lista3 = [1,2,3,4,5]

soma = list(map(lambda x,y: x+y, lista2,lista3))
print((soma))

equacao = list(map(lambda a,b,x: a*x+b, [1,2,3],[4,5,6],[0,0,0]))
print(equacao)