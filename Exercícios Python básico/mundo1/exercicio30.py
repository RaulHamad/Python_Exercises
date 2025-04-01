#leia um numero e diga se eh par ou impar

numero = int(input('digite um numero: '))
if numero % 2 == 0:
    print('{} é par'.format(numero))
else:
    print('{} é impar'.format(numero))