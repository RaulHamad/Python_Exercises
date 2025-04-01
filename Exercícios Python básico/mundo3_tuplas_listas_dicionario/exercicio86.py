#crie um programa que crie uma matriz de dimensao 3x3
#  e preencha com valores lidos pelo teclado. no final mostre a 
# matriz na tela com a formatacao correta.



print('=' *20)
print('Exercicio 86')
print('=' *20)


"""lista = [[], [], []]
m = 0
for c in range(0,3):
    lista[0].append(int(input(f'Digite a posição [{m},{c}]: ')))
   
m += 1
for c in range(0,3):
    lista[1].append(int(input(f'Digite a posição [{m},{c}]: ')))
m += 1    
for c in range(0,3):
    lista[2].append(int(input(f'Digite a posição [{m},{c}]: ')))
    

print(lista[0])
print(lista[1])
print(lista[2])"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'[{linha},{coluna}]: '))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()