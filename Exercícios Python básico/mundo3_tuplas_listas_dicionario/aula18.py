dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

#tupla ()
#lista []
#dicionarios {}

dados = dict() # dados = {}
dados = {'nome':'Pedro','idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' #inserir elemento ao dicionario
print(dados)
del dados['idade'] # eliminar o elemento idade
print(dados)

filme = {'titulo': 'Star Wars', 'ano': 1987, 'diretor': 'George lucas'}
print(filme.values()) # printa os valores star wars , 1987, George lucas
print(filme.keys()) #printa titulo ano e diretor
print(filme.items()) # retorna todo conjunto de dicionario

for k, v in filme.items():
    print(f' o {k} é {v}')

pessoas = {'nome': 'gustavo', 'Sexo': 'M', 'Idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]}')
for c in pessoas.items():
    print(c)
for c in pessoas.values():
    print(c)
for c in pessoas.keys():
    print(c)
pessoas['nome'] = 'leandro'
pessoas['peso'] = 98.5
print(pessoas)