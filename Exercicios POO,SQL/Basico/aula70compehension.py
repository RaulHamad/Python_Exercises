     
nums = [1,2,3,4,5,6,7,8,9,10,12,13]
lista =[x*2 for x in nums if (x % 2==0)]
print(lista)

lista1= [[1,2,3],[4,5,6],[7,8,9]]
[[print(num) for num in lista] for lista in lista1]
#criando matriz
matriz = [[num for num in range(0,3)]for listaa in range(0,3)]

print(matriz)
[print(num) for num in lista1]
[[print(num) for num in a]for a in lista1]
#dict comprehension
dicio = {'a':1,'b':2,'c':3,'d':4}
quadrado ={chave:valor**2 for chave, valor in dicio.items() if not valor%2}
print(quadrado)
cubo = {c: v**3 for c,v in dicio.items()}
print(cubo)
#set comprehension
numero = {x for x in range(1,6)}
print(numero)

num ={1,2,3,3,1,5,4,6,2,1}
numero = {x for x in range(1,7)}
print(numero)
conjunto = {x for x in num}
print(conjunto)
quadrado ={x**2 for x in conjunto}
print(quadrado)

frase = 'Treinamento python aeiou'.replace(' ','')
letras = {letra for letra in frase}
print(letras)