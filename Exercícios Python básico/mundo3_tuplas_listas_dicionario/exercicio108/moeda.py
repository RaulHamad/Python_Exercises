def aumentar(n, p=0):
    n = ((n*p) /100) + n
    return n

def diminuir(n,p=0):
    n = n - ((n*p) /100)
    return n



def dobro(n):
    return n*2
def metade(n):
    n /= 2
    return n

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')



