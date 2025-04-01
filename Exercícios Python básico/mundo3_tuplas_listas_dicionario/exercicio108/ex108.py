
# Exercicio 108 - adapte o codigo do ex107 criando uma funcao adicional
#chamada moeda() que consiga mostrar os valores como um valor monetario formatado


import moeda



n = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10%, de {moeda.moeda(n)} temos {moeda.moeda(moeda.aumentar(n,10))}')
print(f'Reduzindo 20%, de {moeda.moeda(n)} temos {moeda.moeda(moeda.diminuir(n,20))}')


