#programa q leia um nome de cidade e dizer se ela tem a primeira palavra santo.

cidade = input('digite a cidade: ')
cidade = cidade.lower().split()
print(cidade)
if cidade[0] == 'santo':
    print('tem o nome santo')
else:
    print('n tem nome santo')