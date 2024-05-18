lista = []

for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    lista.append(num)

tupla = tuple(lista)

print(tupla[::-1])
