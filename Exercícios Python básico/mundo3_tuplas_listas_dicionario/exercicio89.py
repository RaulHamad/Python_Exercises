#crie um programa que leia nome e duas notas de varios
#  alunos e guarde tudo em uma lista composta. 
# no final mostre um boleim contendo a media de cada um e permita
#  que o usuario possa mostrar as notas de cada aluno individualmente.


print('=' *20)
print('Exercicio 89')
print('=' *20)

lista_nome =list()
lista_nota = []
lista_media = list()
lista_boletim = []
contador = 0

while True:
    nome = str(input('Digite o nome: '))
    lista_nome.append(nome)
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    lista_nota.append(nota_1)
    lista_nota.append(nota_2)
    lista_media.append((nota_1+nota_2)/2)
    lista_nome.append(lista_nota[:])
    lista_boletim.append(lista_nome[:])
    lista_nome.clear()
    lista_nota.clear()
    contador += 1
    print('Deseja continuar? [S/N]: ', end=' ')
    continuar = str(input(' ')).strip().lower()
    while continuar not in 'sn':
        print('opção inválida...')
        print('Deseja continuar? [S/N]: ', end=' ')
        continuar = str(input(' ')).strip().lower()
    if continuar in 'n':
        break

print(lista_boletim)
print(lista_media)
print('-='*30)
print('No', end='        ')
print('NOME', end= '            ')
print('MÉDIA')  
print('-='*30)

for c in range(0, contador):
    for n in range(0, contador):
        if n == 0:
            print(f'{(c+1):<} {lista_boletim[c][n]:^20} {lista_media[c]:>7}')

print('Mostrar notas de qual aluno? (999 finaliza programa): ', end=' ')
continuar = int(input(' '))
while continuar != 999:
    for c in range(1, contador +1):
        for l in range(1,contador +1):
            if (continuar) == (l):
                print(f' Aluno: {lista_boletim[continuar -1][0]}.  Notas: {lista_boletim[(continuar -1)][1]}', end=' ')
                print(f'  Média: {lista_media[(continuar -1)]}')   
        break
    print('-='*30)
    print('Mostrar notas de qual aluno? (999 finaliza programa): ', end=' ')
    continuar = int(input(' '))
    print('-='*30)


            
        
    