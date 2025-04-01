#crie um modulo chamado moeda.py que tenha as funções incorporadas
#aumentar(), diminuir(), dobro(), metade().
#faça tambem um programa que importe esse modulo e use algumas dessas funções.
# Exercicio 108 - adapte o codigo do ex107 criando uma funcao adicional
#chamada moeda() que consiga mostrar os valores como um valor monetario formatado


import moeda



n = float(input('Digite o preço: '))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Aumentando 10%, de R${n} temos R${moeda.aumentar(n,10)}')
print(f'Reduzindo 20%, de R${n} temos R${moeda.diminuir(n,20)}')


