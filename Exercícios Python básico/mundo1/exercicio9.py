#pedir numero e mostrar sua tabuada de multiplicar

numero = int(input('digite um numero inteiro: '))
for resultado in range(1, 11):
    print('{} * {:2} = {}'.format(numero, resultado, (numero*resultado)))