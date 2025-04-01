import pandas as pd

df = pd.read_csv("05_05_imdb_titulos.csv")
print(df["title"])
print(df["year"] > 1950)

print(df.head(10))#head visualiza as primeiras filas
print(df.tail())
print(" ")
print(df.size)