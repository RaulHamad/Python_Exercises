#leia um numero n inteiro e mostra os n primeiros termos da sequencia de fibonacci


print( '\º/' *10)
print('Bem vindo')
numero = int(input('Quantos termos: '))
n_anterior = 0
sequencia_total = 1
sequencia = sequencia_total 
contador = 1
print(n_anterior)
    
while contador != numero:
    print(sequencia_total)
    contador += 1
    sequencia_total = sequencia + n_anterior
    n_anterior = sequencia
    sequencia = sequencia_total
        