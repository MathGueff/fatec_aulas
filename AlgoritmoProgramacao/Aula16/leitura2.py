with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.split())

print("Fim do arquivo")