#leia 6 numeros e some os que forem par

"""numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))
numero3 = int(input('digite um numero: '))
numero4 = int(input('digite um numero: '))
numero5 = int(input('digite um numero: '))
numero6 = int(input('digite um numero: '))
lista = (numero1,numero2,numero3,numero4,numero5,numero6)"""
contador = 0
for c in range(1,7):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        contador += numero
print('a soma dos numeros pares sao {}'.format(contador))


