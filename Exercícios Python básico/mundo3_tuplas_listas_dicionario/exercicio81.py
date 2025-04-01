#crie um programa que vai ler varios
#  numeros e colocar em uma lista. Depois disso:
#A) quantos numeros foram digiitados
#B) a lista de valores ordenada de forma decrescente
#C) se o valor 5 foi digitado e esta ou nao na lista


print('=' *20)
print('Exercicio 81')
print('=' *20)

lista = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    print('Deseja continuar [S/N]?', end=' ')
    sim_nao = input('').strip().lower()
    while sim_nao not in 'sn':
        print('Opção inválida...')
        print('Deseja continuar [S/N]?', end=' ')
        sim_nao = input('').strip().lower()
    if sim_nao == 'n':
        break


lista.sort(reverse=True)
print('Programa Finalizado...')
print(f'Foram digitados {len(lista)} numeros')
print(f'A ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O numero 5 nao esta na lista')
