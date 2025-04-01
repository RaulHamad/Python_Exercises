#faca um programa que tenha uma função chamada maior(),
# que receba varios parametros com valores inteiros.
#Seu programa tem que analisar todos os valores
# e dizer qual deles é o maior.
import time


print('=' *20)
print('Exercicio 99')
print('=' *20)

def maior(*itens):
    
    print('Analisando os valores....')
    time.sleep(0.5)
    for c in itens:
        print(f'{c}',end=' ')
    if itens == ():
        print('O maior valor é 0')
    else:
        print(f'. O maior valor é {max(itens)}')

maior(1,5)
maior(3,6,8,1,2,0,4)
maior(9,5,100,25,30,45)
maior()