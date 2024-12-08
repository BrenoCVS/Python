import random
import os
def adivinhacao():
    numero = random.randint(1, 10)
    tentativas = 0
    limpar_tela()
    print("Foi sorteado um número de um 1 a 10")
    print("Você deve adivinhar que número é esse")
    print("Você terá 5 tentativas!")

    while True:
        try:
            if tentativas > 5:
                        limpar_tela()
                        print("Você perdeu!")
                        continuar()
                        break
            palpite = int(input("Esolha um número de 1 a 10:  "))
            tentativas += 1

            if 1 <= palpite <= 10:
                if(palpite > numero):
                    limpar_tela()
                    print("Você escolheu um número muito alto. Tente novamente.")
                elif(palpite < numero):
                    limpar_tela()
                    print("você escolheu um número muito baixo. Tente novamente.")
                else:
                    limpar_tela()
                    print("Parabens! você acertou o número escolhido! Você precisou de ",tentativas," tentativas")
                    continuar()
                    break
        except ValueError:
            print("Entrada inválida. Porfavor digite um número inteiro.")
            continuar()
            break

def continuar():
    resposta = input("Deseja jogar novamente? (s/n) ").strip().lower()

    if resposta == "n":
        print("Obrigado por jogar!")
        return False
    elif resposta == "s":
        resposta = ""
        adivinhacao()
    else:
        print("Opção inválida!")
        
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    adivinhacao()