#ler ano de nascimento de sete pessoas e mostrar quantas
#atingiram a maioridade
import datetime

ano = datetime.date.today().year
cont = 0
cont2 = 0
for c in range(1,8):
    ano_nascimento = int(input('qual ano de nascimento: '))
    if (ano - ano_nascimento) < 21:
        cont += 1
        print('a pessoa nascida em {} n é de maior'.format(ano_nascimento))
    else:
        cont2 += 1
        print('a pessoa nascida em {}  é de maior'.format(ano_nascimento))
print('{} sao de maior e {} nao sao de maior'.format(cont2, cont))