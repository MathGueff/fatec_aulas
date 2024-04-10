while True:
    frase_inicial = ""
    frase = input("Digite uma frase: ").lower()
    frase_strip = frase.strip() # Retira os espaços nos extremos
    frase_split = frase_strip.split() # Retira os espaço entre a frase, transforma ela em uma lista
    for palavra in frase_split:
        frase_inicial = frase_inicial + palavra # Usado para recriar a frase inicial sem os espaços que foram tirados no frase.split()
    frase_inversa = frase_inicial[::-1] # Faz a string ficar invertidada
    if(frase_inicial == frase_inversa):
        print("UAU, é um palíndromo!!!!!!")
        break
    else:
        print("Infelizmente não é um palíndromo")