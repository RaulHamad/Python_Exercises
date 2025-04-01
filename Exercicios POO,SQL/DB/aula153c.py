import sqlite3

con = sqlite3.connect("empresa.db")
cur = con.cursor()

exp_sql = "INSERT INTO competencias (nome,area) Values (?,?)"
registros = [("Configurar linha de Produção","PRODUÇÃO"),
             ("Elaborar plano de marketing","MARKETING"),
             ("Vender para Mercosul", "VENDAS"),
             ("Realizar a manutenção da LP","PRODUÇÃO"),
             ("Operar CAD e CAM","ENGENHARIA")]

for registro in registros:
    con.execute(exp_sql, registro)

con.commit()


cur.close()