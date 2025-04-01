velocidade = int(input('digite a velocidade do carro: '))

if velocidade > 80:
    print('voce foi multado em {} reais'.format((velocidade - 80) * 7))
else:
    print('siga viagem')