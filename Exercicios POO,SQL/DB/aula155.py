import sqlite3

con = sqlite3.connect("empresa.db")
cur = con.cursor()

exp_sql = """SELECT matricula,nome FROM funcionarios WHERE sexo = 'M'"""

cur.execute(exp_sql)

linha = cur.fetchone()
print(linha)
linha = cur.fetchone()
print(f'Matricula: {linha[0]:5d}, Nome: {linha[1]}')

con.close()