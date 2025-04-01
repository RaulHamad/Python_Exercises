#faca um programa que tenha uma funcao chamada ficha() que
#receba dois parametros opcionais: o nome de um jogador e quantos 
#gols ele marcou.O programa devera ser capaz de mostrar a 
#ficha do jogador, mesmo que algum dado nao tenha
#sido informado corretamente.

print('=' *20)
print('Exercicio 103')
print('=' *20)

def ficha(player, gols=0):
    if nome == '':
        player = '<desconhecido>'
    if gol == '':
        gols = 0
    return (f'O jogador {player} fez {gols} gols.')

nome = (input('Nome do jogador: ')).strip()
gol = (input('Quantos gols: ')).strip()
print(ficha(nome,gol))