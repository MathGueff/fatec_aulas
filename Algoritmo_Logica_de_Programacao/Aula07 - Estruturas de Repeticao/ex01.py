n = int(input("Digite um valor: "))
e1 = 0
e2 = 0
qtd = 1

print("=====================")
# Usando FOR
for i in range(1, n+1):
    e1 = e1 + 2 ** i
print(f"O valor de E é igual a {e1} (usando for)")

# Usando WHILE
while qtd <= n:
    e2 = e2 + 2 ** qtd
    qtd = qtd + 1
print(f"O valor de E é igual a {e2} (usando while)")
