#docstrings ( comentarios explicando as funções para outras pessoas)
#help(input) #descrição de ajuda

def contador(i=0,f=0,p=0):#valores opcionais caso n seja declarado
    """
    -> faz uma contagem e mostra na tela
    i=inicio
    f= fim
    p=passo
    return = nao tem retorno
    """
    c=i
    while c <=f:
        print(f'{c}',end=' ')
        c += p
    print('fim!')

contador(1,10,1)