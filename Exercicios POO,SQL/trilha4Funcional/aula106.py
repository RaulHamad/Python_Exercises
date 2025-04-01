def dobro(x):
    return x*2
def quadradro(x):
    return x*x

def calcular(operacao, lista, funcao):
    print(f'calculando: {operacao}')
    for y in lista:
        print(f'{y} --> {funcao(y)}')

calcular('dobro de 1 a 5', range(1,6),dobro)
calcular('quadrado de 1 a 5', range(1,6), quadradro)