#Escreva um programa que pergunte a quantidade de Km 
# percorridos por um carro alugado e a quantidade de 
# dias pelos quais ele foi alugado. Calcule o preço a pagar,
#  sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


km_percorridos = float(input('digite quantos km foram percorridos: '))
dias_alugados = float(input('quantos dias o carro foi alugado: '))
preco_diaria = 60 * dias_alugados
preço_km = 0.15 * km_percorridos
print('um carro alugado por {}dias e que percorreu {}km, ira pagar um total de {} reais'.format(dias_alugados, km_percorridos, (preço_km + preco_diaria)))