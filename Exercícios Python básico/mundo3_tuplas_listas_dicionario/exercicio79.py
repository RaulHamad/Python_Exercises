#Crie um programa onde o usuario possa digitar varios valores
#  numericos e cadastre-os em uma lista. Caso o numero exista
#  la dentro , ele nao sera adicionado. No final exiba todos
#  os valores em ordem numerica.


print('=' *20)
print('Exercicio 79')
print('=' *20)

lista = list()
Numero = int(input('Digite um numero: '))
print('Numero cadastrado') 
lista.append(Numero)
while True:
    print('Quer continuar? [S/N]', end=' ')
    continuar = input(' ').strip().lower()
    if continuar not in 'sn':
        print('Opção inválida...')
    else:
        if continuar == 's':
            Numero = int(input('Digite um numero: '))
            if Numero not in lista:
                print('Numero cadastrado')
                lista.append(Numero)
            else:
                print('Numero Duplicado... nao cadastrar')    
        if continuar == 'n':
            break
        
lista.sort()  
print(lista)

    

