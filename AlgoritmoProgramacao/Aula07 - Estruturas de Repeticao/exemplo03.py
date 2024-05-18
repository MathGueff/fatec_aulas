qnt = 0
frase = input("Digite uma frase: ")

"""for letra in frase:
    if(letra == "a" or letra == "ã" or letra == "â"):
        qnt_a = qnt_a + 1
        
print(f"A frase digitada contém {qnt_a} de letras A")"""

for letra in frase.lower():
    if letra in "aeiouáàãâéóõòúùû":
        qnt = qnt + 1
print(f"A frase digitada contém {qnt} vogais")