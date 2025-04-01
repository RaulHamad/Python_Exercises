#ler um numero entre 0 e 9999 e mostrar separado unidade,dez, centena e milhar

numero = input('Digite um valor entre 0 e 9999: ')

print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))