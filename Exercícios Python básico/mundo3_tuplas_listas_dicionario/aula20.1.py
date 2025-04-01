def soma(a=0,b=0,c=0):
    s=a+b+c
    return s
r1 = soma(3,2,5)
r2 = soma(1,2)
r3 = soma(6,7,8)
print(f'Os resultados foram {r1}, {r2} e {r3}')

def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f *= c
    return f

f1 = fatorial(5)
print(f1)
