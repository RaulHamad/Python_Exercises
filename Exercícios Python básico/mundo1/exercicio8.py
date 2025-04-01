#ler numero em metros e exibir em centimetros e milimetros

numero_metros = float(input('digite um numero em metros: '))
numero_centimetros = numero_metros * 100
numero_milimetros = numero_metros * 1000
print(' {} metros são {} centimetros  e {} milimetros'.format(numero_metros, numero_centimetros, numero_milimetros))