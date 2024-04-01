# Calculando os anos, meses, semanas e DIAS de vida de uma pessoa

nasc = int(input("Digite o ano em que voce nasceu: "))
ano_atual = int(input("Digite o ano atual (não sei pegar pelo código ainda):"))

anos = ano_atual-nasc
meses= (ano_atual*12) - (nasc*12)
semanas= (ano_atual*52) - (nasc*52)
dias= (ano_atual*365) - (nasc*365)
print("=================")
# Idade em anos
print(f"A idade sua em anos PODE SER {anos} anos")

# Idade em meses
print(f"Já em meses, é {meses} meses")

# Idade em semanas
print(f"Agora em semanas, deve ser {semanas} semanas")

# Idade em dias
print(f"E por fim, em dias, é {dias} dias")