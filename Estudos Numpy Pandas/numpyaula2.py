import numpy as np

m = np.random.randint(10,size=(3,3))# 10 numeros inteiros, 3,3 uma matriz
print(m)
n = np.random.rand(2,2)#para numeros decimais
print(n)
n = np.random.rand(5)#para numeros decimais
print(n)

n = np.random.choice([3,5,9,5,1])#obter uma dos valores
print(n)
n = np.random.choice([3,5,9,5,1],size=(2,3))#obter uma dos valores
print(n)
#obter uma dos valores em probabilidade, P = soma tem q ser 1
n = np.random.choice([2,4,6],p=[0.5,0.5,0.0],size=(5))#obter uma dos valores em probabilidade

print(n)



a