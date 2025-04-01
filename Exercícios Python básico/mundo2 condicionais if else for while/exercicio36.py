#programa para aprovar emprestimo para compra de uma casa
# pedir valor da casa, salario, quantos anos quer pagar
#calcule o valor da prestacao sabendo que n pode exceder 30% do salario


valor_casa = float(input('digite valor da casa: '))
valor_salario = float(input('digite seu salario '))
anos_a_pagar = float(input('quer pagar em quantos anos: '))
prestacao = valor_casa / (anos_a_pagar * 12)

if prestacao <= (valor_salario * (30 / 100)):
    print('emprestimo aprovado. serao {} parcelas de R${}'.format((anos_a_pagar * 12), (prestacao)))
else:
    print('a parcela de R${} é maior do que 30% do seu salario'.format(prestacao))
    print('emprestimo n aprovado')
    