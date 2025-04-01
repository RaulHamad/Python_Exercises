def somar(x):
    def calcular(y):
        return x+y
    return calcular

soma1 = somar(5)
soma2 = somar(10)#x

print(soma1(5))#y
print(soma2(5))