#faca um programa q tenha uma função que receba as
# dimensoes de um terreno retangular e mostre a area do terreno
print('=' *20)
print('Exercicio 96')
print('=' *20)
def area_terreno(l,c):
    area = l*c
    print(f' A area de um terrno {l}m por {c}m é de {area}m2.')

print('Controle de terrenos')
print('-'*30)
l= float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))  
area_terreno(c,l)

