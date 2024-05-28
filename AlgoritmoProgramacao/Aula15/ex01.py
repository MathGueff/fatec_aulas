from random import choice

escolha = ["pedra", "papel", "tesoura"]

def exibir_resultados():
    print(f"Escolha do player: {escolhaP}")
    print(f"Escolha do bot: {bot}")
    print("======")

while True:
    bot = choice(escolha)
    escolhaP = (input("Digite pedra, papel ou tesoura ou 1 para sair: ")).lower()

    if(escolhaP != "pedra" and escolhaP != "tesoura" and escolhaP != "papel" and escolhaP != "1"):
        print("Digite um dos três apenas!")
        continue

    if(escolhaP == "1"):
        break

    if(escolhaP == bot):
        print("Empate!")
        exibir_resultados()
        continue

    if(escolhaP == "pedra" and bot == "tesoura"):
        print("Player ganhou!")
        exibir_resultados()
        continue
    elif(escolhaP == "papel" and bot == "pedra"):
        print("PLayer ganhou!")
        exibir_resultados()
        continue
    elif (escolhaP == "tesoura" and bot == "papel"):
        print("Player ganhou!")
        exibir_resultados()
        continue
    else:
        print("Player perdeu")
        exibir_resultados()
        continue
