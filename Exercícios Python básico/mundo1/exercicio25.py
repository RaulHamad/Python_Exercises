#programa q leia um nome de pessoa e dizer se ela tem a palavra silva.

cidade = input('digite a cidade: ')
cidade = cidade.lower().split()
print(cidade)
if 'silva' in cidade:
    print('tem o nome silva')
else:
    print('n tem nome silva')