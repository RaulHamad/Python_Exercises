arquivo = open('texto2.txt')

print((arquivo.read()))
arquivo.seek(10)#move o cursor para posicao indicada 
print((arquivo.read()))
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)