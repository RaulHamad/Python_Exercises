arquivo = open('texto3.txt', 'w')# apaga tudo q tinha e escreve 
# A escreve sem apagar o que ja esta feito
while True:
    fruta = input('Digite uma fruta: ')
    if fruta == 'sair':
        break
    else:
        arquivo.write(fruta)
        arquivo.write('\n')
arquivo.close()
print(arquivo.closed)