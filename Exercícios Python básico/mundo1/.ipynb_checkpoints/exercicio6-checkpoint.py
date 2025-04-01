#leia um numero e calcula o dobro, triplo e raiz quadrada do numero

number = float(input('digite um numero: '))
number_double = number * 2
number_triple = number * 3
number_raiz = number ** (1/2)
print(' o dobro de {} é {}, o triplo é {} e a raiz quadrada é {}'.format(number,number_double, number_triple, number_raiz))