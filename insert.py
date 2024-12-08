# pip install psycopg2
#Esse codigo de cima tem que colocar no terminal da máquina

#importando o conector do mysql
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

    #pedindo para o usuario escrever um nome, que será gravado no banco de dados
    nome = input("Escreva uma nome: ")

    #guardando o comando sql em uma variavel. O %s serve para passarmos os valores depois
    inserir_nome = "INSERT INTO teste (nome) VALUES (%s)"

    #esse é o valor que irá no lugar do %s
    valor = (nome,)

    #esse cursor é uma variavel do próprio conn, que vai se ligar com o banco de dados. Igual o stmt do php
    cursor = conn.cursor()

    #Aqui ta preparando o cursor para executar o comando sql e passando o valfor que irá substituir o %s 
    cursor.execute(inserir_nome, valor)

    #Aqui ele executa
    conn.commit()

    print("Nome inserido na tabela")

    #Após gravar no banco de dados ele fecha o cursor
    cursor.close()

except OperationalError as erro:

    #Caso de errado ele cai no except e mostra essa mensagem
    print(f"Falha ao inserir nome: {erro}")

finally:
    #Aqui ele ta testando se o conn consguiu estabelecer conexão com o banco de dados 
    if 'conn' in locals() and conn is not None:
        #Caso tenha estabelecido a conexão, ele encerra a conexão e fecha as variáveis
        cursor.close()
        conn.close()
