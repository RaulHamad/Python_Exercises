#programa q ler varios numeros inteiros.
# o programa vai continuar perguntando ate que o usuario digite 999.
# mostre quantos numeros foram digitados e a soma entre eles.

print('=-=' * 10)
print('helo world')
print('Exercicio66')
print('=-=' * 10)

soma = contador = 0

while True:
    numero = int(input('Digite um numero[999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Voce digitou {contador} numeros')
print(f' a soma entra eles é {soma}')