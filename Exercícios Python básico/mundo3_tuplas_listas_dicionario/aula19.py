def mensagem(msg):
    print('-------------------------')
    print(msg)
    print('-------------------------')

mensagem('Sistema e alunos')

def title(txt):
    print('-'*40)
    print(txt)
    print('-'*40)

title('curso em video')
title(10)

def area(a,b):
    #a= float(input('Digite o lado do retangulo:'))
    #b= float(input('Digite a altura do retangulo: '))
    area = a * b
    print(area)


area(a=2,b=5)# posso explicitar o parametros A e B ou inverter
area(b=2,a=5)

#empacotamento
def contador (*num):
    for c in num:
        print(c)
    print(num)

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)


def lista(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

valores= [6,3,9,1,0,2]
lista(valores)
