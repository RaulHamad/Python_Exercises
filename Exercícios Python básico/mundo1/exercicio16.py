#crie um numero real e exiba sua parte inteira
import math
numero_real = float(input('digite um numero real: '))
numero_inteiro = math.trunc(numero_real)
print('a parte inteira do numero {} é {}'.format(numero_real, numero_inteiro))