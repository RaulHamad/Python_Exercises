#crie um programa que gerencie o aproveitamento de uma
#  jogador de futebol. O programa vai ler o nome do jogador
#  e quantas partidas ele jogou. Depois vai ler a quantidade
#  de gols feitos em cada partida. No final, tudo isso sera
#  guardado em um dicionario incluindo o total de gols feitos
#  durante o campeonato.


print('=' *20)
print('Exercicio 93')
print('=' *20)


dados = dict()
gols = list()

dados["nome do jogador"] = str(input('Qual o nome do jogador: '))
dados["partidas"] = int(input(f'Quantas partidas {dados["nome do jogador"]} jogou: '))
for c in range(dados['partidas']):
    gols.append(int(input(f'Gols da partida {c+1}: ')))
   
dados["gols"] = gols[:]
dados["total"] = sum(gols)
print(dados)
print('='*30)
print(f'O jogador {dados["nome do jogador"]} jogou {dados["partidas"]} partidas')
for c,k in enumerate(gols):
    print(f'=> Na partida {c+1}, fez {k} gols')
print(f'Foi um total de {dados["total"]} gols')
