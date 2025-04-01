#leia um ano e diga se eh bissexto
import calendar

ano = int(input('digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('{} é bissexto'.format(ano))
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('{} é bissexto'.format(ano))
else:
    print('{}  não é bissexto'.format(ano))