#crie um programa q tenha uma tupla unica com nomes de produtos e seus
#respectivos preços na seqeuncia. no final mostre uma listagem de preços
#organizando os dados em forma tabular.



print('=' *20)
print('Exercicio 76')
print('=' *20)

tupla = ('Pão', 1.75, 'Arroz', 5.2, 'Macarrão', 10,
 'Chocolate', 9.99)
"""print(f'{tupla[0]:.<30}R${tupla[1]:>5.2f}')
print(f'{tupla[2]:.<30}R${tupla[3]:>5.2f}')
print(f'{tupla[4]:.<30}R${tupla[5]:>5.2f}')
print(f'{tupla[6]:.<30}R${tupla[7]:>5.2f}')"""
for lista in range(0,len(tupla)):
    if lista % 2 == 0:
        print(f'{tupla[lista]:.<30}',end='')
    else:
        print(f'R$ {tupla[lista]:>5.2f}')