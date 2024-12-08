# Função para salvar a mensagem no banco de dados
def salvar_mensagem_no_banco(mensagem):
    """Salva a mensagem no banco de dados PostgreSQL."""
    try:
        # Conectar ao banco
        conexao = psycopg2.connect(**db_config)


        consulta = "SELECT * FROM sessao"
    
        #Abrindo o cursor 
        cursor = conexao.cursor()

        #Preparando o cursor para executar o SQL
        cursor.execute(consulta)

        #Colocando todos os resultados do select dentro da variavel linhas
        linhas = cursor.fetchall()

        for linha in linhas:

            # Capturar a data e hora atual
            data = datetime.now()

            # Formatar para o padrão 'DD-MM-YYYY'
            data_formatada = data.strftime('%d-%m-%Y %H:%M:%S')

            # Inserir a mensagem e a data na tabela 'mensagem'
            query = "INSERT INTO mensagem (traducao, data_formatada, cod_usuario) VALUES (%s, %s, %s)"
            cursor.execute(query, (mensagem, data_formatada, linha[1]))

            # Confirmar a inserção no banco de dados
            conexao.commit()

            print("Mensagem salva no banco de dados com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao salvar a mensagem no banco de dados: {e}")
    finally:
        if conexao:
            cursor.close()
            conexao.close()