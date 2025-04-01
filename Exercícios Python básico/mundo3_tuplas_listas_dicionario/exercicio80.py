#crie um programa onde o susuario possa digitar cinco valores numericos
# e cadastre-os em uma lista, ja na posicao correta sem usar o sort().
#no final mostre a lista ordenada na tela.




print('=' *20)
print('Exercicio 80')
print('=' *20)


lista = []

for c in range(0,5):
    item = int(input('Digite um valor: '))
    if c == 0 or item > lista[-1]:
        lista.append(item)
        print(lista)          
    else:
        pos = 0
        while pos < len(lista):
            if item <= lista[pos]:
                lista.insert(pos, item)
                break
            pos += 1
        
          

       
print(lista)