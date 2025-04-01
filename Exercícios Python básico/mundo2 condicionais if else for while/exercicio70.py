#crie um programa que leia o nome e o preço de varios produtos.
#o programa devera perguntar se o usuario vai continuar.
#No final, mostre:
#a) qual e o total gasto na compra
#B) quantos produtos custam mais de R$1000
#C) qual e o nome do produto mais barato


print('=-=' * 10)
print('helo world')
print('Exercicio70')
print('=-=' * 10)

contador_cadastro = 0
contador_gastos = contador_preço = 0
while True:
    contador_cadastro += 1
    print(f'--Cadastrando produto {contador_cadastro}--')
    nome = input('Nome do produto: ')
    preco = float(input('qual o preço: '))
    contador_gastos += preco
    if preco > 1000:
        contador_preço += 1
    if contador_cadastro == 1:
        produto_mais_barato = preco
        nome_do_produto_barato = nome
    if preco < produto_mais_barato:
        produto_mais_barato = preco
        nome_do_produto_barato = nome
    print('Deseja continuar?')
    continuar = input('[S/N]: ').strip().upper()[0]
    
    while continuar not in 'SN':
        continuar = input('[S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print('FIM !!!')
print(f'o total gasto na compra foi de R${contador_gastos} reais')
print(f'{contador_preço} produtos custaram mais de R$1000')
print(f' o produto mais barato foi o {nome_do_produto_barato}')


    