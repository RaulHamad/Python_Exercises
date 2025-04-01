#ler 3 numeros e dizer qual o maior entre eles

numero_1 = int(input('digite um numero: '))
numero_2 = int(input('digite um numero: '))
numero_3 = int(input('digite um numero: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(numero_1, ' e maior')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(numero_2, ' e maior')
elif numero_3 > numero_1 and numero_3 > numero_2:
    print(numero_3, 'é maior')
else:
    print('sao iguais')