#desnvolver um programa que leia o NOME, Idade e Sexo de 4 pessoas
#mostre a media de idade do grupo
# qual é o homem mais velho
#quantas mulheres tem menos de 20 anos

media_idades = 0
maior_idade = 0
mais_velho = 0
contador_sexo = 0
for contador in range(1,5):
    nome_das_pessoas = input('qual o nome da pessoa {}: '.format(contador))
    idade_das_pessoas = int(input('Digite a idade da pessoa {}: '.format(contador)))
    sexo_das_pessoas = input('digite "M" para masculino ou "F" para feminino: ').lower()
    media_idades +=  idade_das_pessoas
    
    if contador == 1:
        maior_idade = idade_das_pessoas
        mais_velho = nome_das_pessoas
    if maior_idade < idade_das_pessoas:
        maior_idade = idade_das_pessoas
        mais_velho = nome_das_pessoas
    if sexo_das_pessoas == 'f' and idade_das_pessoas < 20:
        contador_sexo += 1

    
print('A media de idade do grupo é de {} anos.'.format(media_idades/contador))
print('A pessoa mais velha do grupo é {}.'.format(mais_velho))
print('No grupo tem {} mulheres com menos de 20 anos.'.format(contador_sexo))