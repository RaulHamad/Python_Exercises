import operator
import random
import time
"""estado1 = {'UF': 'Rio de janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'Soa Paulo', 'Sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['Sigla'])
print(brasil[1]['UF'])"""

"""estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for c in brasil:
    for d in c.keys(): # for mostrando UF e
        print(d)


print('-= '*30)
print('-='*30) # itemgettet para deixar em ordem crescente/decrescente

dados = {"Jogador 1" : random.randint(1,6), "Jogador 2": random.randint(1,6)
, "Jogador 3": random.randint(1,6), "Jogador 4": random.randint(1,6) }

rank = list()
for c, k in dados.items():
    time.sleep(1)
    print(f'O {c} tirou {k}')
rank = sorted(dados.items(),key=operator.itemgetter(1), reverse=True)

for c,k in enumerate(rank):
    print(f'{c+1}º Lugar: {k[0]} tirando {k[1]}')"""

#uso do .get para verificar se existe a key no dicionario(padrao é NONE)
pessoa = {
    'Nome' : 'Raul',
    'Sobrenome': 'Hamad'
}
print(pessoa['Sobrenome'])
print(pessoa.get('apelido'))
print(pessoa.get('Nome'))
import copy
x = copy.deepcopy(pessoa) #cria uma copia profunda (deepcopy)
#shalow copy copia o dict mas apenas os imutaveis
# **kwargs para argumentos nomeados(dicionario)
def mostro_argumentos(*args, **kwargs):
    for chave valor in kwargs.items():
        print(chave,valor)
mostro_argumentos(1,2,'nome':'joana')