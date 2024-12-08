import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        database='python',
        user='root',
        password='mydba')
    
    consulta = "SELECT * FROM teste"
    cursor = conn.cursor()
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print("Dados retornados:")
    for linha in linhas:
        print("id: ", linha[0])
        print("nome: ", linha[1])
except Error as e:
    print("Erro ao realixar consulta ",e)
finally:
    if(conn.is_connected()):
        conn.close()
        cursor.close()