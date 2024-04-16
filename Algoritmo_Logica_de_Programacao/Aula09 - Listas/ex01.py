numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número : ")))

print(f"O maior valor da lista é: {max(numeros)} e está na posição {numeros.index(max(numeros))}")
