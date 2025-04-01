#crie um programa q vai ler varios numero e colocar em uma lista
# depois disso, crie duas listas extras que vao conter apenas os valores 
#pares e os valores impares digitados
# ao final mostre as 3 listas



print('=' *20)
print('Exercicio 82')
print('=' *20)

lista = []
lista_par = []
lista_impar = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    if lista[-1] % 2 == 0:
        lista_par.append(lista[-1])
    else:
        lista_impar.append(lista[-1])
    print('Deseja continuar? [S/N]', end=' ')
    sim_nao = str(input('')).strip().lower()
    if sim_nao == 'n':
            break
    while sim_nao not in 'sn':
        print('ERROUUU... tente novamente:')
        sim_nao = str(input('Deseja continuar? [S/N] ')).strip().lower()
        

print(f'Os valores digitados foram{lista}')
print(f' os valores pares sao {lista_par}')
print(f'os valores impares sao {lista_impar}')