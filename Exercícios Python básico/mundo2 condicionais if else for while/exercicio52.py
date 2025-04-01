#leia um numero e diga se ele é ou nao um numero primo

numero = int(input('digite o numero: '))
contador = 0
for c in range(1, numero +1):
     if numero % c == 0:
        contador += 1
    
if contador == 2:
    print('{} é primo'.format(numero))
        


