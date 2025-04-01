#crie um programa que tenha uma tupla com varias palavras(n usar acentos)
#depois disso, voce deve mostrar para cada palavra quais sao as suas vogais.

print('=' *20)
print('Exercicio 77')
print('=' *20)


tupla = ('pao', 'raul', 'toto', 'makunouchi', 'ippo')

for lista in tupla:
    print(f'\nNa palavra {lista} temos: ', end='')
    for letras in lista:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
 
