a = lambda x,y : x*y

print(a(3,4))

s = lambda x,y,z : x+y+z if z >= 5 else x+y-z

print(s(2,3,5))

#criar funcao lambda em linha

print((lambda x,y,z : x+y+z if z >= 5 else x+y-z)(5,5,1))

def comprimento():
    titulo = 'Sr(a) '
    acao = (lambda x : titulo +x)
    return acao

comprimentar = comprimento()
print(comprimentar('Raul'))