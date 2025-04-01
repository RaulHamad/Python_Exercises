#programa q calcula a soma entre todos os numeros impares
#que sao multiplos de 3 e que se encontram no intervalo entre 1 ate 500

contador_inicial = 0
for c in range(1, 501,2):
    if c % 3 == 0:
        contador_inicial = c + contador_inicial
print(contador_inicial)
