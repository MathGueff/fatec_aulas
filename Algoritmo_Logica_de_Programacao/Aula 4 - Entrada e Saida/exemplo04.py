# Convertendo Celsius em Fahrenheit e Kelvin

print("\n======Vamos converter Cº em Fº======")

c = float(input("Digite a temperatura em Cº: "))
f = (9*c+160)/5
k= c + 273.15

print(f"A temperatura em Fahrenheit é {f}")
print(f"Mas se for em Kelvin é: {k}")
print("==================")
print(f"{c} Cº")
print(f"{f}ºF")
print(f"{k} K")
print("==================")
# Fazendo a conversão contrária agora (F para C)
print("Agora vamos converter de F para C")

f = int(input("Valor do Fahrenheit: "))
c = (f*5-160)/9

print(f"O valor de Celsius é: {c}")