#leia 3 comprimentos de reta e diga se forma um triangulo

reta_1 = int(input('digite um numero: '))
reta_2 = int(input('digite um numero: '))
reta_3 = int(input('digite um numero: '))

if reta_1 + reta_2 > reta_3 and reta_2 + reta_3 > reta_1 and reta_1 + reta_3 > reta_2:
    print(' formam um triangulo')
else: 
    print('nao forma triangulo')