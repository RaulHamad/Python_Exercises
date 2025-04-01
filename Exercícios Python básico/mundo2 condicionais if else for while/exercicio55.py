#ler o peso de cinco pessoas e mostrar qual foi o maior e menor peso lido.
pesomaior = 0
pesomenor = 0
for c in range(1,6):
    peso = float(input('qual seu peso pessoa {}: '.format(c)))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    if pesomaior < peso:
        pesomaior = peso
    if pesomenor > peso:
        pesomenor = peso
       
print('O maior peso é {} e o menor {}'.format(pesomaior,pesomenor))