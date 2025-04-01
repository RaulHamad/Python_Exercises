
# AS TUPLAS SAO IMUTAVEIS

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[3]) #mostra o item numero 3 da tupla
print(lanche[1:3]) # mostra os itens 1 a 2 da tupla
print(lanche[-1]) # mostra ultimo item da tupla
print(len(lanche))
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi demais!!!!')

for contador in range(0, len(lanche)):
    
    print(f'eu vou comer {lanche[contador]} na posicao {contador}')

for posicao, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posicao {posicao}')

print(sorted(lanche)) # organiza a tupla em ordem alfabetica


a= (2, 5, 4)
b = (5, 8, 1, 2)
c = a+ b
print(min(a))# mostra o menor numero dentro da tupla
print(max(a)) # mostra o maior numero dentro da tupla


print(c) 
print(len(c))
print(c.count(5)) # conta quantas vezes aparece o numero 5 na tupla
print(c.index(8)) # em que posicao esta o numero 8 na tupla


nome = 'José'
idade = 33
salario = 987.3

print(f'O {nome:.^10} tem {idade} e ganha R${salario:.2f}')
#:.2f - aumenta os 0 das cadas decimais
#:>20 alinha a direita com 20 espaços
#:<10 - alinha a esquerda com 10 espaços
#:-<10 alinha variavel a esquerda e completa os espaços com -
#:-^10 - centralizado com 10 -