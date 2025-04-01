#pergunte a distancia em km. se for ate 200km cobre R$0,50 por km, 
# se nao cobre R$0,45 por km

distancia_km = int(input('qual a distancia da viagem: '))

if distancia_km <= 200:
    print('voce pagará {} reais'.format(distancia_km * 0.50))
else:
    print('voce pagará {} reais'.format(distancia_km * 0.45))
