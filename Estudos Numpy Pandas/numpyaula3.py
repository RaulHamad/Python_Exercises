import numpy as np


m = np.array([[1,1,2],[4,2,3]])
print(m)
print(" ")
print(np.sum(m,axis=0))
print(" ")
n= np.array([[8,8,7],[7,7,8]])
print(np.concatenate([m,n], axis=1))
print(" ")
print(np.ptp(m))#subtrai o maior valor pelo menor da matriz
print(" ")
print(np.percentile(m,100))

print(np.median(m))#mediana
print(np.mean(n))#media aritmetica
print(np.average(n))#media ponderada

