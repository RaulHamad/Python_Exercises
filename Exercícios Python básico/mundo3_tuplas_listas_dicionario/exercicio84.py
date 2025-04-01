#faca um programa q leia nome e peso de varias pessoas,
#guardando tudo em uma lista. no final motre:
#a) quantas pessoas foram cadastradas
#b) uma listagem com as pessoas mais pesadas
#c) uma listagem com as pessoas mais leves
#70kg as mais leves e 100kg as mais pesadas
print('=' *20)
print('Exercicio 84')
print('=' *20)


lista =[]
peso_min = []
peso_max = []
cadastro = list()
maior = menor = 0
while True:
    lista.append(str(input('Digite seu nome: ')))
    lista.append(int(input('Digite seu peso: ')))
    if len(cadastro) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] < menor:
            menor = lista[1]
        if lista[1] > maior:
            maior = lista[1]
    cadastro.append(lista[:])
    lista.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    if continuar == 'n':
            print('operação finalizada')
            break
    while continuar not in 'sn':
        print('Opção inválida... ', end=' ')
        continuar = input('Deseja continuar? [S/N]: ').strip().lower()
    if continuar == 'n':
        print('operação finalizada')
        break   
print('-=' *30)
print('-=' *30)
print(f'Foram cadastradas {len(cadastro)} pessoas:')
print(f'O maior peso foi {maior}: ', end= ' ')
for c in cadastro:
    if c[1] == maior:
        print(c[0],)
print(f'O menor peso foi {menor}: ', end= ' ')
for c in cadastro:
    if c[1] == menor:
        print(c[0],)

