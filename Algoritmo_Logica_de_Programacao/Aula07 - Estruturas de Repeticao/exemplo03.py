qnt_a = 0
qnt_espaco = 0
frase = input("Digite uma frase: ")

for letra in frase.lower():
    if(letra == "a" or letra == "ã" or letra == "â"):
        qnt_a = qnt_a + 1
    elif(letra == " "):
        qnt_espaco = qnt_espaco + 1
print(f"A frase digitada contém {qnt_a} de letras A e {qnt_espaco} espaços")