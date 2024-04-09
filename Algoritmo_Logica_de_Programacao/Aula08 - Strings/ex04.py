while True:
    frase = input("Digite uma frase: ").strip()
    palavras = frase.split()
    frase1 = ""
    for palavra in palavras:
        frase1 = frase1 + palavra
    frase2 = frase1[::-1]
    if frase1 == frase2:
        palindromo = True
    else:
        palindromo = False

    if(palindromo):
        print("UAU, é um palíndromo!")
        break
    else:
        print("Não foi dessa vez")
        print("=================")

# Verificando se uma frase é palíndroma