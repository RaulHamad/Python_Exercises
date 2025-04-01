from mysql.connector import connect

con = connect(
    host="localhost",
    port=3306,
    user="root",
    password="6whfimam"
)

print(type(con))

con.close()


