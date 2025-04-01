#crie um programa onde 4 jogadores joguem um dado e tenham 
# resultados aleatorios. guarde esses resultados
# em um dicionario. No final coloque esse dicionaio em 
# ordem sabendo que o vencedor tirou o maior numero no dado.




print('=' *20)
print('Exercicio 91')
print('=' *20)

import random
import time
import operator

dados = {"Jogador 1" : random.randint(1,6), "Jogador 2": random.randint(1,6)
, "Jogador 3": random.randint(1,6), "Jogador 4": random.randint(1,6) }

rank = list()
for c, k in dados.items():
    time.sleep(1)
    print(f'O {c} tirou {k}')
rank = sorted(dados.items(),key=operator.itemgetter(1), reverse=True)

for c,k in enumerate(rank):
    print(f'{c+1}º Lugar: {k[0]} tirando {k[1]}')




