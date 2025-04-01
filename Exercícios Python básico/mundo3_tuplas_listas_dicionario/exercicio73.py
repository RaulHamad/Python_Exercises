#crie uma tupla preenchida com os 20 primeiros times da tabela do campeonato brasileiro
#  na ordem de colocação. depois mostre:
#a) apenas os 5 primeiros colocados
#b) os ultimos 4 colocados da tabela
#c) uma lista com os times em ordem alfabetica
#D) em que posição esta o time da Botafogo-RJ.



print('=' *20)
print('Exercicio 73')
print('=' *20)

tabela_brasileirao = ('Palmeiras-SP', 'Internacional-RS', 'Fluminense-RJ',
 'Corinthians-SP', 'Flamengo-RJ', 'Atletico Paranaense-PR', 'Atletico Mineiro-MG',
  'Fortaleza-CE', 'Sao Paulo-SP', 'América-MG', 'Botafogo-RJ', 'Santos-SP',
   'Goias-GO', 'Bragantino-SP', 'Coritiba-PR', 'Cuiaba-MT', 'Ceara-CE', 'Atletico-GO',
    'Avai-SC', 'Juventude-RS')
print(len(tabela_brasileirao))
print('Os cinco primeiros colocados')
for contador in tabela_brasileirao[0:5]:
    print(contador)
print('Os quatro ultimos colocados')
for contador in tabela_brasileirao[-5:]:
    print(contador)
print(sorted(tabela_brasileirao))

print(tabela_brasileirao.index('Botafogo-RJ') +1)
