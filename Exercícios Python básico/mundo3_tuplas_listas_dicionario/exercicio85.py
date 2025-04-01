#crie um programa onde o usuario possa digitar sete valores numericos
# e cadastre-os em uma lista unica que mantenha separados os valores
#pares e impares.No final mostre os valores pares e impares 
# em ordem crescente

print('=' *20)
print('Exercicio 85')
print('=' *20)


"""lista_par = list()
lista_impar = list()
valores = list()

for c in range(0, 7):
    valores.append(int(input('Digite um numero: ')))
    if valores[0] % 2 == 0:
        lista_par.append(valores[:])
    else:
        lista_impar.append(valores[:])
    valores.clear()
valores.append(lista_par[:])
valores.append(lista_impar[:])
print(valores)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares sao {valores[0]}')
print(f'Os valores impares sao {valores[1]}')"""

lista = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input('Digite um numero: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista.sort()
print(lista[0])
print(lista[1])