#aprimore o desafio anterior mostrando no final: 
# a) a soma de todos os valores pares digitados
#  b) a soma dos valores da terceira coluna 
# C) o maior valor da segunda linha



print('=' *20)
print('Exercicio 87')
print('=' *20)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite numero da linha [{linha},{coluna}] '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
    print()
print(soma)
print(matriz[0][2] + matriz[1][2] + matriz[2][2])
print(max(matriz[1]))

