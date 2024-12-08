import mysql.connector
from mysql.connector import Error
import configparser

def criar_conexao():
    config = configparser.ConfigParser()
    
    if not config.read("config.ini"):
        print("Não foi possível encontrar o arquivo config.ini.")
        return None
    
    try:
        conn = mysql.connector.connect(
            host=config['conexao']['host'],
            database=config['conexao']['database'],
            user=config['conexao']['user'],
            password=config['conexao']['password']
        )
        if conn.is_connected():
            print("Conexão estabelecida com sucesso!")
        return conn
    
    except Error as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None  