from random import randint
m = []
l = []
soma = 0
total = 0

for y in range(5): #Cria cada linha
    for x in range(5): #Preenche cada linha
        l.append(randint(1, 100))
    m.append(l)
    l = []

for l in range(5):
    if((l)%2 == 0): #Descobre se a linha é par ou não
        for c in range(5):
            soma = soma + m[l][c]
            total = total + m[l][c]
    else:
        for c in range(5):
            total = total + m[l][c]

media = soma/total
print(m)
print(f"A soma das linhas pares é {soma}")
print(f"A média de {soma}/{total} é igual a {media:.2f}")


