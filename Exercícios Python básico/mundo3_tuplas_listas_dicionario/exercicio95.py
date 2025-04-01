#aprimore o desafio 93 para que ele funcione com varios
#  jogadores, incluindo um sistema de visualização
#  de detalhes do aproveitamento de cada jogador.


print('=' *20)
print('Exercicio 95')
print('=' *20)

dados = dict()
gols = []
jogadores = []

while True:
    dados["Jogador"] = str(input('Digite o nome do atleta: '))
    dados["Partidas"] = int(input('Quantas partidas: '))
    for c in range(dados['Partidas']):
        gols.append(int(input(f'Gols da partida {c+1}: ')))
    dados["Total Gols"] = gols[:]
    gols.clear()
    jogadores.append(dados.copy())
    continuar = str(input('Deseja adicionar outro jogador?[S/N]: ')).strip().lower()
    while continuar not in 'sn':
        print('Opção inválida...')
        continuar = str(input('Deseja adicionar outro jogador?[S/N]: ')).strip().lower()
    if continuar == 'n':
        break    
print('='*45)
print('  cod nome',end='           ')
print('gols',end='             ')
print('Total')
print('='*45)
for c in range(len(jogadores)):
    print(f'  {(c):>2} {(jogadores[c]["Jogador"]):<12} {(jogadores[c]["Total Gols"])}       {sum(jogadores[c]["Total Gols"])}')
while True:
    print('Mostrar dados de qual jogador?[999 encerra programa]',end='')
    detalhe = int(input(''))
    if detalhe == 999:
        break
    if detalhe >= len(jogadores):
        print('Opção inválida...')
    if detalhe in range(0,len(jogadores)):
        print('='*40)
        print(f'Detalhe do jogador {jogadores[detalhe]["Jogador"]}')
        print(f' O jogador {jogadores[detalhe]["Jogador"]} marcou {sum(jogadores[detalhe]["Total Gols"])} em {jogadores[detalhe]["Partidas"]} jogos.')
        print('='*40)

