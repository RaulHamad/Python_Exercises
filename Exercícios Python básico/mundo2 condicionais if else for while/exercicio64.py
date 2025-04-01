#programa q ler varios numeros inteiros.
# o programa vai continuar perguntando ate que o usuario digite 999.
# mostre quantos numeros foram digitados e a soma entre eles.


print( '\º/' *10)
print('Bem vindo')
print( '\º/' *10)
print('Exercicio 64')
print( '\º/' *10)
numero = int(input('Quantos um numero inteiro [999 para parar]: '))
contador = 0
n_soma = 0
contador_soma = 0

while numero != 999:
    contador += 1
    n_soma += numero
    numero = int(input('Quantos outro numero inteiro[999 para parar]: '))
    
print('FIM')
print('total de {} numeros e a soma entre eles foi {}'.format(contador, (n_soma)))