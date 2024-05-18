from random import randint
jogadas = [] #Vai guardar 6000 posições
resultados = [0]*7 #Vai guardar apenas 7 posições

for i in range(6000):
    sort = randint(1, 6)
    jogadas.append(sort)
    resultados[sort] = resultados[sort] + 1

print("As 6000 jogadas foram feitas, vamos ver como está sua sorte!")
for i in range(6):
    print(f"A frequência em que o valor {i+1} apareceu foi de: {jogadas.count(i+1)/6000:.2f}% e apareceu um total de {jogadas.count(i+1)} ")

print("===========Usando a lista RESULTADOS===========")
for i in range(6):
    print(f"A frequência em que o valor {i+1} apareceu foi de: {resultados[i+1]/6000:.2f}%")
print(resultados)