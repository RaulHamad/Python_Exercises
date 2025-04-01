#ler um preço e mostrar com 5% desconto

preco_normal = float(input('digite o valor do produto: '))
preco_desconto = preco_normal - (preco_normal * (5/100))
print('o preço normal é de {} e com 5% de desconto fica {}'.format(preco_normal, preco_desconto))