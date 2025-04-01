#cria um programa q le o nome completo da pessoa
#mostre o nome com todas as letras maiusculas e minusculas
#quantas letras ao todo sem considerar os espaços
#quantas letras tem o primeiro nome

nome = input('digite um nome completo: ')
print(nome.upper())
print(nome.lower())

nome2 = nome.replace(' ', '')
print(len(nome2))

nome = nome.split()
print(nome)
print(len(nome[0]))
