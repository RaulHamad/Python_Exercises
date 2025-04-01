dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)
pessoas = []
#pessoas.append(dados) copia uma lista mas o que mudar na lista dados muda
#automaticamente na lista pessoas
pessoas.append(dados[:]) # cria copia independente para pessoas
print(pessoas)
dados.insert(1, 22)
print(dados)
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[0][1])
print('-=' *30)
"""teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)"""
# Galera.clear() - limpa os dados da lista 
galera = [ ['Joao', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[2][1])
print('-=' *30)
for p in galera:
    print(p)
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade')