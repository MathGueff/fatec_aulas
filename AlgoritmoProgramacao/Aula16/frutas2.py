with open("frutas.txt","a", encoding="utf-8") as arquivo:
    frutas = []
    while True:
        fruta = input("Digite uma fruta: ")
        frutas.append(fruta)
        if fruta.lower() == "sair":
            break
        else:
            arquivo.write(fruta)
            arquivo.write("\n")