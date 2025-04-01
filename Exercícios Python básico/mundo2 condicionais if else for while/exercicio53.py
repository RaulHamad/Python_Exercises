#palindromo

palavra = str(input('digite uma palavra: '))
palavra_junta = palavra.strip().replace(' ', '').upper()
print(palavra_junta)
cont = ''
for c in range (len(palavra_junta) -1, -1 , -1):
    print(palavra_junta[c])
    if palavra_junta == c:
        print('{} = a {}'.format(palavra_junta, c))