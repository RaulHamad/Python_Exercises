#faca um programa que tenha uma funcao chamada contador() 
#e que receba tres parametros: inicio,fim e passo e
# realize a contagem.
#seu programa tem que realizar tres contagem atraves da funcao criada:
#A) de 1 ate 10 de 1 em 1
#b) de 10 ate 0 de 2 em 2
#c) uma contagem personalizada

import time

print('=' *20)
print('Exercicio 98')
print('=' *20)

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            time.sleep(0.5)
        print()
        print('='*40)
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            cont -= p
            time.sleep(0.5)
        print()
        print('='*40)


  


        
contador(1,10,1)
contador(10,0,2)

i= int(input('Digite o inicio: '))
f= int(input('Digite o fim: '))
p= int(input('Digite o intervalor: '))
contador(i,f,p)
