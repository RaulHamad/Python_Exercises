#faca um programa que leia um numero e mostre seu fatorial
import math
"""n1 = int(input('Digite um numero inteiro: '))
contador_fatorial = 1
for c in range(1,n1+1):
    contador_fatorial = contador_fatorial * c
    
print('{}! é igual a {}'.format(n1,contador_fatorial))"""

"""n1 = int(input('Digite um numero inteiro: '))
contador = 1
fatorial = 1
while contador != n1 +1 :
    fatorial = fatorial * contador
    contador += 1
    
print('{}! é igual a {}'.format(n1,fatorial))"""

n1 = int(input('Digite um numero inteiro: '))
fatorial = math.factorial(n1)
print(fatorial)