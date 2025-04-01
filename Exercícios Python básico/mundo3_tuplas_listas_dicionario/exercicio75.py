#desenvolva um programa q leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final mostre:
#A) quantas vezes apareceu o valor 9.
#B) em que posicao foi digitado o primeiro valor 3.
#C)quais foram os numeros pares.

print('=' *20)
print('Exercicio 75')
print('=' *20)

n1 = (int(input('Digite um numero: ')),
 int(input('Digite outro: ')),
  int(input('Digite outro: ')),
   int(input('Digite outro: ')))

tupla = (n1)
print(f'O numero 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'o primeiro valor 3 esta na posição {tupla.index(3)+1}')
else:
    print('Nao tem numero 3 digitado.')
print('Os numeros pares são:', end='')
for n in tupla:
    if n %2 == 0:
        print(n, end=' ')
   

    




