# pip install psycopg2
#Esse codigo de cima tem que colocar no terminal da máquina

#importando o conector 
import psycopg2

#importanto a variavel de erro da biblioteca do conector
from psycopg2 import OperationalError

try:
    #passando as parâmetros de conexao do banco de dados
    conn = psycopg2.connect(
        host='localhost',
        database='python',
        user='postgres',
        password='postdba'
    )
    #A partir daqui vc vai por dentro do metodo de inserção
    #Criando o script SQL
    consulta = "SELECT * FROM sessao"
    
    #Abrindo o cursor 
    cursor = conn.cursor()
    
    #Preparando o cursor para executar o SQL
    cursor.execute(consulta)

    #Colocando todos os resultados do select dentro da variavel linhas
    linhas = cursor.fetchall()

    
    #imprimindo os resultados
    print("Dados retornados:")
    for linha in linhas:
        #Aqui vc vai colocar o insert. Dentro desse for
        print("id: ", linha[0])
        print("nome: ", linha[1])
    #A partir daqui vc n coloca no metodo
except Error as e:
    print("Erro ao realixar consulta ",e)
finally:
    if(conn.is_connected()):
        conn.close()
        cursor.close()