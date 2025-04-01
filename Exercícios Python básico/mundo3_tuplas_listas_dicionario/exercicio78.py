#faça um programa qye leia 5 valores numericos 
# e guarde-os em um lista. No final mostre o maior e
#  menor numero e suas posicoes.

print('=' *20)
print('Exercicio 78')
print('=' *20)

lista = list() # ou pode ser lista = []
for c in range(0,5):
    lista.append(int(input('Digite um numero: ')))


print(f'O menor valor é {min(lista)} e esta na posição : ', end=' ')
for c, x in enumerate(lista):
    if x== min(lista):
        print(f'{c}', end=' ')
print(f'\nO maior valor é {max(lista)} e esta na posição : ', end=' ')
for c, x in enumerate(lista):
    if x== max(lista):
        print(f'{c}', end=' ')