#leia varios numeros inteiros pelo teclado.
# no final mostre a media entre todos os numeros, o maior e o menor valor
# o programa deve perguntar se o usuario quer continuar ou nao




print( '\º/' *10)
print('Bem vindo')
print( '\º/' *10)
print('Exercicio 65')
print( '\º/' *10)

contador =  maior_valor = menor_valor = soma = 0
continuar = 'S'

while continuar in 'Ss':
    numero = int(input('Digite outro inteiro: '))
    contador += 1
    soma += numero
    if contador == 1:
        maior_valor = menor_valor = numero
    if maior_valor < numero:
        maior_valor = numero
    
    if numero < menor_valor:
        menor_valor = numero 
    continuar = input('Quer continuar[S/N]: ').upper().strip()[0]
    
    
  
print('FIM')
print(f'foi lido {contador} numeros')
print(' o menor valor foi {}'.format(menor_valor))
print(' o maior valor foi {}'.format(maior_valor))
print('a Media foi de {}'.format(soma/contador))

