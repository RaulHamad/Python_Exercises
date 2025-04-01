#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
#depois disso, mostr a listagem de numeros gerados
#  e tambem indeque o menor e o maior valor que estao na tupla.

import random

print('=' *20)
print('Exercicio 74')
print('=' *20)

print('Gerando cinco numeros aleatorios')

tupla = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10) )
print(tupla)
menor = tupla[0]
maior = tupla[0]
for c in tupla:
    if c > maior:
        maior = c
    if menor > c:
        menor = c
print(f'O menor é {menor}')
print(f'O maior é {maior}')
print(f'O menor é {min(tupla)}')
print(f'O maior é {max(tupla)}')

