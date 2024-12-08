import os

contatos = []

def carregarContatos():
    if os.path.exists("contatos.txt"):
        with open("contatos.txt", "r") as arquivo:
            for linha in arquivo:
                nome, telefone, email = linha.strip().split(";")
                contatos.append({"nome": nome, "telefone": telefone, "email": email})

def salvarContatos():
    with open("contatos.txt", "w") as arquivo:
        for contato in contatos:
            arquivo.write(f"{contato['nome']}; {contato['telefone']}; {contato['email']}\n")

def adicionarContatos():
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o telefone do contato: ").strip()
    email = input("Digite o email do contato: ").strip()

    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)

    print(f"✅ Contato '{nome}' adicionado com sucesso!")
    salvarContatos()

def listarContatos():
    if not contatos:
        print("Nenhum contato salvo.")
    else:
        print("\n Lista de Contatos")
        for i, contato in enumerate(contatos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
    print()

def buscarContato():
    nomeBuscar = input("Digite o nome que deseja buscar: ").strip().lower()
    encontrados = [contato for contato in contatos if nomeBuscar in contato['nome'].lower()]

    if encontrados:
        print("Contatos Encontrados:")
        for contato in encontrados:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Nenhum contato encontrado.")
    print()

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
            adicionarContatos()
        elif opcao == 2:
            limpar_tela()
            listarContatos()
        elif opcao == 3:
            limpar_tela()
            buscarContato()
        elif opcao == 4:
            print("Programa encerrado.")
            break
        else: 
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    carregarContatos()
    menu()