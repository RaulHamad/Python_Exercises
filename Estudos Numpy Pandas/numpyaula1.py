import numpy as np

print(np.__version__)

#criando array

meu_array = np.array([1,2,3,4,5])
print(type(meu_array))
print(meu_array.dtype)

array_duas_dimensoes = np.array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3],[3,4,5],[6,7,8]]])
print(array_duas_dimensoes)

#soma, min e max array

print(np.sum(array_duas_dimensoes))
print(np.amax(array_duas_dimensoes))
print(np.amin(array_duas_dimensoes))
print(np.min(array_duas_dimensoes))
print(np.max(array_duas_dimensoes))
print(np.pi,np.e)

a = np.zeros(10)
#array de zero e de 1
zero= np.zeros([2,3])
um = np.ones([3,4])
print(a)
print(zero)
print(um)
#array identidade
identidade = np.identity(5)
print(identidade)

#ARANGE

cinco = np.arange(5)
print(cinco)
cinco = np.arange(3,16,2)
print(cinco)

#linspace são gerados valores, linearmente espaçados:
# coloca o intervalo e depois a quantidade de numeros a aparecer

lins = np.linspace(1,11,100)
print(lins)

criar_array_arange = np.arange(10)
criar_2 = np.reshape(criar_array_arange,[5,2])

print(criar_array_arange)
print(criar_2)
print(criar_array_arange.reshape(2,5))
print(criar_2.shape)#tipo de matriz
print(criar_2.size)#quantidade de valores
#matriz com 3 dimensoes
matriz_3d = np.arange(32).reshape(4,4,2)
print(matriz_3d)
#localizacao de elementos
print(matriz_3d[2,0])
print(np.sort(matriz_3d))
print(np.array(matriz_3d+2))#somar multiplicar matrizes

print(np.array(matriz_3d >10))

#matriz 1 dimensao

m1 = np.array([90,7,9,4,2,1])
m2 = np.array([11,34,67,99,55,66])
print(np.sort(m1))
print(np.concatenate((m1,m2)))
print(np.multiply(m1,m2))
print(np.divide(m1,m2))
print(np.around(12.256,2))# arredonda casa decimais


for i in range(5):
    print(i)
else:
    print("done")
