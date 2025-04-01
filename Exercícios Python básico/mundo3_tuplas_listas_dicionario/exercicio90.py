#faça um programa q leia nome e media de um aluno,
#  guardando tambem a situação em um dicionario. 
# no final mostre o conteudo da estrutura na tela.



print('=' *20)
print('Exercicio 90')
print('=' *20)


dados ={}
lista =[]
contador = 0
while True:
    dados['Nome'] = str(input('Digite o nome: '))
    dados['Média'] = float(input('Digite a média: '))
    if dados['Média'] >= 7:
        dados['Situação'] = 'Aprovado'
    else:
        dados['Situação'] = 'Reprovado'
    lista.append(dados.copy())
    contador +=1
    print('Deseja continuar? [S/N]', end='')
    cont = str(input(' ')).strip().lower()
    while cont not in 'sn':
        print('opção inválida...')
        print('Deseja continuar? [S/N]: ', end=' ')
        cont = str(input(' ')).strip().lower()
    if cont in 'n':
        break
for c in range(0, contador):
    print(f' O aluno {lista[c]["Nome"]} tem média {lista[c]["Média"]}')
    print('-=' *5)
    print(f'Está{lista[c]["Situação"]}')
    print('-=' *5)
    