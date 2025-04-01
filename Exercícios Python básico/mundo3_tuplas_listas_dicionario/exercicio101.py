#crie um programa que tenha uma funcao chamada voto() que
# va ireceber como parametro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa 
#tem voto Negado,Opcional ou Obrigatorio nas eleições.



print('=' *20)
print('Exercicio 101')
print('=' *20)

def voto(ano):
    import datetime
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano
    if idade < 18:
        print(f'Sua idade é {idade} e tem voto Negado')
    elif idade >= 18 and idade < 65:
        print(f'Sua idade é {idade} e seu voto é Obrigatorio')
    elif idade >= 65:
        print(f'Sua idade é {idade} e seu voto é Opcional')

p1 = voto(int(input('Qual seu ano de nascimento: ')))


