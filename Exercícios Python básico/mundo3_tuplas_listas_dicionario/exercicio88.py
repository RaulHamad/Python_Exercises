#faça um programa que ajude um jogador da mega sena a criar palpites.
#  o programa vai perguntar quantos jogos serao gerados e vai
#  sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando
#  tudo em uma lista composta.


print('=' *20)
print('Exercicio 88')
print('=' *20)

import random
from time import sleep

lista = []
palpite = list()

quant_palpites = int(input('Quantos jogos voce quer? '))

for c in range(0, quant_palpites):
    for x in range(0,6):
        palpite.append(random.randint(1,61))
        
    palpite.sort()
    lista.append(palpite[:])
    
    palpite.clear()
for d in range(0,quant_palpites):
    print(f'Gerando jogo {d+1}: {lista[d]}')
    sleep(1)

