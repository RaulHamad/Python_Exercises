import pandas as pd

# df = pd.read_csv("makunouchi.csv")
# print(df)
# print(" ")
# convertir = pd.read_excel("makunouchi.xlsx")
# convertir.to_csv("Makunouchi.csv",index=None,header=True)
# print(convertir)

df = pd.read_csv("makunouchi.csv")
print(df)

#coordenada de localização

print(df.iloc[1,3])
print(df.iloc[2,3])
print(df.iloc[2,:3])

#localizar

print(df.loc[1,"SEMESTRE"])
print(df.loc[2,"EDAD"])
print(df.loc[:3,("NOMBRE")])

#adicionar colunas

df["TURNO"] = pd.Series(["Manha","noche","tarde","noche"])
print(df)

#RETIRAR COLUNA .POP

semestre = df.pop("SEMESTRE")
print(df)

#INSERIR UMA FILA

df = df._append(pd.Series(["Carlos",22,"M","Engenero","noche"],index=["NOMBRE","EDAD","GENERO","CARRERA","TURNO"]),ignore_index=True)
print(df)

#DELETANDO LINHAS ESPECIFICAs
print(" ")
print(df.drop([1,2]))

#FILTRAR DADOS

print(df[(df["GENERO"] == "F") & (df["EDAD"] >= 22)])
#FILTRAR UMA PALAVRA DENTRO DA STRING
print(df[df["NOMBRE"].str.contains("ia")])

