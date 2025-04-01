import pandas as pd
import numpy as np


data = {"NOMBRE":["Maria","Joao","Jose","Ippo"],
        "Carrera": ["Auditoria","Informatica","Derecho","Idiomas"]}

print(pd.DataFrame(data))

df = pd.DataFrame([4,9,2,6,10,200],columns=["Naranjas"])
print(df)
df = pd.DataFrame([["toto",4],["IPPO",9]],columns=["Nombre","Edad"])
print(df)

df = pd.DataFrame(np.random.randn(4,3),columns=["a","b","c"])
print(df)

df = pd.read_csv("05_05_imdb_titulos.csv")
print(df.head(10))

#visualizar todas as linhas

print(df.to_string())