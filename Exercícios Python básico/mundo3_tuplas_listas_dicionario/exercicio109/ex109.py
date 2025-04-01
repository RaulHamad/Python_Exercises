
# modifique as funções que foram criadas no desafio 107 para que elas
#aceitem um parametro a mais, informando se o valor retornado por elas vai
# ser ou não formatado pela função moeda() desenvolvida no desafio 108



import moeda



n = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n,True)}')
print(f'O dobro de {moeda.moeda(n)} é {(moeda.dobro(n,True))}')
print(f'Aumentando 10%, de {moeda.moeda(n)} temos {(moeda.aumentar(n,10,True))}')
print(f'Reduzindo 20%, de {moeda.moeda(n)} temos {(moeda.diminuir(n,20,True))}')


