with open("idades.txt", "r") as entrada:
    linhas = entrada.readlines()

idades = []
sexos = []
totalIdades = 0.0

for linha in linhas:
    campos = linha.split(",")
    idade = int(campos[0])
    sexo = campos[1]
    idades.append(idade)
    sexos.append(sexo[0])
    totalIdades += idade

total_idade_f = 0
total_idade_m = 0
qtd_f = 0
qtd_m = 0

for i in range(len(idades)):
    if(sexos[i] == "F"):
        qtd_f += 1
        total_idade_f += idades[i]
    else:
        qtd_m += 1
        total_idade_m += idades[i]

idade_media_f = total_idade_f/qtd_f
idade_media_m= total_idade_m/qtd_m
print("----------")
print(f"O total das idades é {totalIdades:.2f}")
print(f"A média das idades é {totalIdades/len(idades):.2f}")
print(f"Sexo feminino: Quantidade: {qtd_f} - Média: {idade_media_f:.2f}")
print(f"Sexo masculino: Quantidade: {qtd_m} - Média: {idade_media_m:.2f}")
print("----------")
