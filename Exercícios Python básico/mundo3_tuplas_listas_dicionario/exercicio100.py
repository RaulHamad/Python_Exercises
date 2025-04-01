#faça um programa que tenha uma lista chamada numero
# e dias funções chamadas sorteia() e somaPAr(). 
#A primeira funcao vai sortear 5 numeros e vai coloca los
# dentro da lista e a segunda funcao vai mostrar a soma
# entre todos os valores pares sorteados pela funcao anterior.


print('=' *20)
print('Exercicio 100')
print('=' *20)

import random
numeros = []

def sorteia(numeros):
   
    for c in range(5):
        numeros.append(random.randint(1,100))
       
    print(numeros)
def somaPar(numeros):
    cont = 0
    for c in range(len(numeros)):
        
        if numeros[c] % 2 == 0:
            cont += numeros[c] 
    print(f'A soma dos pares é {cont}')

print(numeros)
sorteia(numeros)
somaPar(numeros)