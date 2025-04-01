#ler um numero e dizer seu seno cosseno e tangente
import math
import cmath

numero = float(input('digite um numero: '))
seno_numero = (cmath.sin(numero))
seno_graus = cmath.cos(seno_numero)
print(seno_numero)
print(seno_graus)