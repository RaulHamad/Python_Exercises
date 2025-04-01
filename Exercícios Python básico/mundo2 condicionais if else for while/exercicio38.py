import datetime

ano_nascimento = int(input('qual ano de nascimento: '))
ano_atual = datetime.date.today().year

if ano_atual - ano_nascimento < 18:
    print('ainda vai se alistar, faltam {} anos'.format(18 - (ano_atual - ano_nascimento)))
elif ano_atual - ano_nascimento == 18:
    print('hora de se alistar')
elif ano_atual - ano_nascimento > 18:
    print('passou do tempo a {}anos'.format((ano_atual - ano_nascimento) - 18))