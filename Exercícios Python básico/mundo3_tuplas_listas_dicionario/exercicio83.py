#crie um programa onde o usuario digite uma expressao qualquer que use
#parenteses. Seu aplicativo devera analisar se a expressao passada esta
#com os parenteses abertos e fechados na ordem correta.



print('=' *20)
print('Exercicio 83')
print('=' *20)

lista = list()
expr =(str(input('Digite a expressao: ')))

for simbolo in expr:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
    else:
        lista.append(')')
        break

print(lista)
if len(lista) == 0:
    print('expressao valida')
else:
    print('expressao invalida') 