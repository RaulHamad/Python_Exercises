#programa que mostre a tabuada de varios numeros um de cada vez 
#para cada valor digitado pelo usuario. 
# O programa encerra quando o numero solicitado for negativo

print('=-=' * 10)
print('helo world')
print('Exercicio67')
print('=-=' * 10)

contador = 0

while True:
    print('Para encerrar digite um numero negativo')
    numero = int(input('Digite um numero: '))
    if numero < 0:
        break
    while contador < 10:
        contador += 1
        print(f'{numero} * {contador:2} = {numero*contador:2}')
    contador = 0