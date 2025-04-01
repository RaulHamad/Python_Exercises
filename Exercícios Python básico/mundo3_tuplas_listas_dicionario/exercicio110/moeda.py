
def aumentar(n=0, p=0, f=False):
    n = (((n*p) /100) + n)
    if f is True:
        f'{moeda(n)}'
    else:
        return n

def diminuir(n=0,p=0, f=False):
    n = n - ((n*p) /100)
    if f is True:
        return f'{moeda(n)}'
    else:
        return n



def dobro(n, f=False):
    if f is True:
        return f'{moeda(n*2)}'
    else:
        return n*2
def metade(n, f= False):
    n /= 2
    if f is True:
        return f'{moeda(n)}'
    else:
        return n

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(n,taxaa=0,taxar=0, f=False):
    txt='RESUMO DO VALOR'
    
    print( '-'*(len(txt)+16))
    print(f'        {txt}')
    print('-'*(len(txt)+16))
    if f is True:
        print(f'Preço analisado: \t{moeda(n)}')
        print(f'Dobro do preço: \t{moeda(dobro(n))}')
        print(f'Metade do preço: \t{moeda(metade(n))}')
        print(f'{taxaa}% de aumento: \t{moeda(aumentar(n,taxaa))}')
        print(f'{taxar}% de redução: \t{moeda(diminuir(n,taxar))}')
    else:
        print(f'Preço analisado: \t{(n)}')
        print(f'Dobro do preço: \t{(dobro(n))}')
        print(f'Metade do preço: \t{(metade(n))}')
        print(f'{taxaa}% de aumento: \t{(aumentar(n,taxaa))}')
        print(f'{taxar}% de redução: \t{(diminuir(n,taxar))}')
