#ler a largura e altura de uma parede , calcular sua area
#  e a quantidade de tinta para pinta-la.
#  cada litra de tinta pinta uma area de 2m2.

altura = int(input('qual a altura da parede: '))
largura = int(input('qual a largura da parede: '))
area_parede = altura * largura
litros_tinta = area_parede / 2
print('a area da sua parede é {}m2, e vai precisar de {} litros de tinta'.format(area_parede,litros_tinta))
