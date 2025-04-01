#crie um programa que leia nome, ano de nascimento e 
# carteira de trabalho
# e cadastre-os (com idade) em um dicionario.Se por acaso a CTPS
#diferente de Zero, o dicionario recebera tambem o ano de 
# contratação
# e o salario. Calcule e acrescente alem da idade , com
#  quantos anos a pessoa vai se aposentar

import datetime



print('=' *20)
print('Exercicio 92')
print('=' *20)

dados = {}
dados["Nome"] = str(input('Digite seu nome: '))
dados["ano de nascimento"] = int(input('Qual ano de nascimento: '))
ano_atual = datetime.date.today().year
dados["idade"] = ( ano_atual - dados['ano de nascimento'])
dados["carteira"] = int(input('Digite sua CNTPs: '))
if dados["carteira"] != 0:
    dados["ano_contratação"] = int(input('Qual ano de contratação (0 não tem): '))
    dados["salário"] = float(input('Qual seu salário: '))
    dados["aposentadoria"] = (dados['ano_contratação'] + 35) - dados['ano de nascimento']
for v,k in dados.items():
    print(f' {v} é {k}')

print(dados)