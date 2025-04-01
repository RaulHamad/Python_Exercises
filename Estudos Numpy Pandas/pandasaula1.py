import pandas as pd
import numpy as np

naranjas = pd.Series([4,9,2,6,10,200])
print(naranjas)
manzanas = pd.Series([60,22,1,79,2,8])
print(manzanas)

colores = pd.Series(["rojo","azul","amarillo","verde","morado"])
print(colores)
print(colores[1:3])

materias = pd.Series({"Matematica":60,"Fisica":100,"Quimica":78})
print(materias)
print(materias["Fisica"])
print(materias[materias<90])

numeros = pd.Series(np.arange(1,10))
print(numeros.size)
print(numeros.index)
print(numeros * 2)

numeros = pd.Series(np.arange(1,10))
print(numeros.max())
print(numeros.describe())

materias = pd.Series({"Matematica":75,"Fisica":100,"Quimica":78})
#organiza em ordem alfabetica o dicionario
print(materias.sort_values())
#em ordem decrescente
print(materias.sort_index())
#em ordem crescente dos indices "KEY"
print(materias.sort_index(ascending=False))

data = 5

serie = pd.Series(data=data,index=[0,1,2,3,4,5])
print(serie)

data_list = ["Messi","CR7","Romario"]
indice_list =["PSG","United","Flamengo"]
print(pd.Series(data=data_list,index=indice_list))