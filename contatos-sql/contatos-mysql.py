import os 
import conexao
conn = conexao.criar_conexao()

def consulta():
    try:
        sql_consulta = "SELECT * FROM contatos"
        cursor = conn.cursor()
        cursor.execute(sql_consulta)
        linhas = cursor.fetchall()
        
        if len(linhas) > 0:
            for linha in linhas:
                print("Id:",linha[0],", Nome:",linha[1],", Telefone:",linha[2],", Email:",linha[3])
        else:
            print("Nenhum contato encontrado")
    except Exception as e:
        print("Erro ao listar contatos ", e)
    finally:
        cursor.close()

def salvarContato(nome, telefone, email):
    try:
        sql_inserir = "INSERT INTO contatos(nome, telefone, email) VALUES(%s,%s,%s)"
        cursor = conn.cursor()
        cursor.execute(sql_inserir, (nome, telefone, email))
        conn.commit()
        print("Contato salvo!")
    except Exception as e:
        print("Erro ao cadastrar contato ",e)
    finally:
        cursor.close()

def adicionarContato():
    try:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")

        salvarContato(nome, telefone, email)
    except Exception as e:
        print("Erro ao adicionar contato ",e)

def buscarContato():
    try:
        pesquisa = input("Digite o nome do contato: ")
        sql_buscar = "SELECT * FROM contatos WHERE nome like %s"
        cursor = conn.cursor()
        cursor.execute(sql_buscar,(pesquisa + '%',))
        linhas = cursor.fetchall()
        if len(linhas) > 0:
            for linha in linhas:
                print("Id:",linha[0],", Nome:",linha[1],", Telefone:",linha[2],", Email:",linha[3])
        else:
            print("Nenhum contato encontrado")
    except Exception as e:
        print("Erro ao procurar contato ",e)
    finally:
        cursor.close()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("\n===  AGENDA TELEFÔNICA ===")
        print("[1] Adicionar novo contato")
        print("[2] Listar todos os contatos")
        print("[3] Procurar contato pelo nome")
        print("[4] Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            limpar_tela()
            adicionarContato()
        elif opcao == 2:
            limpar_tela()
            consulta()
        elif opcao == 3:
            limpar_tela()
            buscarContato()
        elif opcao == 4:
            print("Programa encerrado.")
            conn.close()
            break
        else: 
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()