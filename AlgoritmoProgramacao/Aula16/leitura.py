arquivo = open("arquivo.txt", "r",encoding= "utf-8")
print("======")
for linha in arquivo:
    print(linha.strip())
    if("batatinha" in linha.lower()):
        print("==================")
arquivo.close()