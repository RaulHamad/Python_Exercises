def aumentar(n, p=0, f=False):
    n = ((n*p) /100) + n
    if f is True:
        f'{moeda(n)}'
    else:
        return n

def diminuir(n,p=0, f=False):
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



