def quadrado(x):
    return lambda : x**2

funcoes = [quadrado(i) for i in range(1,6)]
for funcao in funcoes:
    print(funcao())