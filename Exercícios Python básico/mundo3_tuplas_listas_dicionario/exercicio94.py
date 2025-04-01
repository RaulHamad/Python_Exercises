#crie um programa que leia nome,sexo e idade de
#  varias pessoas, guardando os dados de cada pessoa
#  em um dicionario e todos os dicionarios em uma lista.
#  no final mostre: 
# a)quantas pessoas foram cadastradas 
#  B) a media de idade do grupo 
# C) uma lista com todas as mulheres
#  D) uma lista com todas as pessoas com idade acima da media


print('=' *20)
print('Exercicio 94')
print('=' *20)

dict = dict()
grupo = list()
cont_idade = 0

while True:
    dict["Nome"] = str(input('Digite um nome: '))
    dict["sexo"] = str(input('Digite o sexo [M/F]:')).strip().lower()
    dict["Idade"] = int(input('Digite a idade: '))
    grupo.append(dict.copy())
    cont_idade += dict['Idade']
    print('Deseja continuar [S/N]: ', end=' ')
    continuar = str(input('')).strip().lower()
    while continuar not in 'sn':
        print('comando inválido...tente novamente')
        print('Deseja continuar [S/N]: ', end=' ')
        continuar = str(input('')).strip().lower()
    if continuar == 'n':
        print('Programa encerrado...')
        break
print(grupo)
print(cont_idade)
print(f'Foram cadastradas {len(grupo)} pessoas')
print(f'A media de idade do grupo é {(cont_idade)/len(grupo):.2f}')
print('As mulheres da lista são: ')
for c in range(0,len(grupo)):
    if grupo[c]["sexo"] == 'f':
        print(grupo[c]["Nome"])
print('As pessoas com idade acima da media são: ')        
for c in range(len(grupo)):
    if grupo[c]["Idade"] > ((cont_idade)/(len(grupo))):
        print(f'{grupo[c]["Nome"]} com {grupo[c]["Idade"]} anos' )
        

