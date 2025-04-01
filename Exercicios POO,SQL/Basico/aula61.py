import aula61_modulo

lista = []
pessoas = []
n = 0

while True:

    sobrenome = aula61_modulo.pega_sobrenome()
    if sobrenome:
        n += 1
        idade = aula61_modulo.pega_idade()
        altura = aula61_modulo.pega_altura()
        peso = aula61_modulo.pega_peso()
        pessoa = [sobrenome,idade,altura,peso]
        lista.append(pessoa)
    else:
        break

print(lista)
lista.sort()
print(lista)
n=0
for i in lista:
    n+= i[1]
media_idade = n/(len(lista))

for i in lista:
    n+= i[3]
media_peso = n/(len(lista))

print(f' a media de idade é {media_idade} e a de peso é {media_peso}')

