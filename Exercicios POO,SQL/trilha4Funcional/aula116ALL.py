#dada uma lista de nomes, verificar se todos começam com a letra "P"
#ANY E ALL - ANY- pelo um argumento true retorna true, all retorna se todos forem true
nomes = ['Petrucia', 'Pedro', 'Paula', 'Piva', 'Pietra']

verificar_letra = all([nome[0]== 'P' for nome in nomes])
print(verificar_letra)
