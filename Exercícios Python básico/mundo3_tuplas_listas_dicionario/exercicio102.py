#crie um programa que tenha uma funcao fatorial()
# que receba dois parametros: o primeiro que indique
# o numero a calcular e o outro chamado show, que sera
# um valor logico(opcional) indicando se sera
# mostrado ou nao na tela o processo de calculo do fatorial.




print('=' *20)
print('Exercicio 102')
print('=' *20)

def fatorial(num=1,show=False):
    """Função para calcular fatorial"""
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        while show == True:
            if show == True and c != 1:
                print(f'{c}',end=' x ')
                break
            if c == 1:
                print(f'{c}',end=' = ')
                break
    return fat
    
n1 = 6
print(fatorial(n1))


