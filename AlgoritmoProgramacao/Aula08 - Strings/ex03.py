
frase = input("Digite uma frase: ")
frase = frase.lower()

# Usando count

a = frase.count("a")
e = frase.count("e")
i = frase.count("i")
o = frase.count("o")
u = frase.count("u")

vogais = a + e + i + o + u

print(f"\nA frase tem {vogais} vogais!")
print(f"""
Vogal a = {a}
Vogal e = {e}
Vogal i = {i}
Vogal o = {o}
Vogal u = {u} """)

# Usando for in
v = 0
for letra in frase:
    if letra in "aeiou":
        v = v + 1

print(f"A frase tem {vogais} vogais")