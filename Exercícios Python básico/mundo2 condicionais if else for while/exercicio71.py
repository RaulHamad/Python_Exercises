#crie um programa q simule um caixa eletronico. 
# pergunte qual o valor o usuario quer sacar(numero inteiro)
#o programa vai informar quantas cedulas de cada valor serao entregues
#obs.: considere que o caixa tem cedulas de R$50, R$20, R$10, R$1

print('=-=' * 10)
print('helo world')
print('Exercicio71')
print('=-=' * 10)
print('Banco Canha')
print('=-=' * 10)
saque = int(input('Qual o valor de saque: '))
valor_total = cont50 = cont20 = cont10 = cont1 =0
while valor_total != saque:
    cont50 += 1
    valor_total += 50
    if valor_total > saque:
        valor_total -= 50
        cont50 -= 1
        if valor_total < saque:
            cont20 += 1
            valor_total += 20
        if valor_total > saque:
            valor_total -= 20
            cont20 -= 1
            if valor_total < saque:
                cont10 += 1
                valor_total += 10
            if valor_total > saque:
                valor_total -= 10
                cont10 -= 1
                if valor_total < saque:
                    cont1 += 1
                    valor_total += 1
                if valor_total > saque:
                    valor_total -= 1
                    cont1 -= 1    


print(f'sao {cont50} cedulas de R$50,00')
print(f'sao {cont20} cedulas de R$20,00')
print(f'sao {cont10} cedulas de R$10,00')
print(f'sao {cont1} cedulas de R$1,00')
print(valor_total)
