#abrir um arquivo, ler e fechar
arquivo = open('texto.txt', 'r')#encoding='utf-8'
print(type(arquivo))
texto = arquivo.read()
print(type(texto))
print(texto)
print(texto)
arquivo.close()