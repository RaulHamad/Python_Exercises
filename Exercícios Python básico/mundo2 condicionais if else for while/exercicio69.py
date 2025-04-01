#criar um programa q leia a idade e o sexo de varias pessoas.
#a cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar
#no final mostre:
#a) quantas pessoas tem mais de 18 anos
#b) quantos homens foram cadastrados
#C) quantas mulheres tem menos de 20 anos

print('=-=' * 10)
print('helo world')
print('Exercicio69')
print('=-=' * 10)

cont_idade = cont_sexo_m = cont_idade_f = 0
while True:
    idade = int(input('Qual a idade: '))
    sexo = input('Qual o sexo [M/F]: ' ).strip().upper()[0]
    while sexo not in 'MF':
        print('opção invalida!')
        sexo = input('Qual o sexo [M/F]: ' ).strip().upper()[0]
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_sexo_m += 1
    if sexo == 'F' and idade < 20:
        cont_idade_f += 1
    print('Deseja continuar?')
    continuar = input('[S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('[S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print('FIM !!!')
print(f' total de pessoas com mais de 18 anos foram {cont_idade}')
print(f'Foram {cont_sexo_m} homens cadastrados')
print(f'São {cont_idade_f} mulheres com menos de 20 anos')