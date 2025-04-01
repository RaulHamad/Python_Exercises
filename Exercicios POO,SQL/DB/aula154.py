import sqlite3

# con = sqlite3.connect("empresa.db")
# cur = con.cursor()
#
# exp_sql = """
#             SELECT matricula, nome, salario FROM funcionarios WHERE sexo = "M"
#             """
# cur.execute(exp_sql)
# #Recupera os registros e guarda em um variavel
# dados = cur.fetchall()
#
# for linha in dados:
#     print(f'Matricula: {linha[0]}, Nome:{linha[1]}, Salario: {linha[-1]}')
#
# con.close()