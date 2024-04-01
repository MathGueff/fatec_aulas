fruta = (input("Digite a fruta desejada: ").capitalize())

if(fruta == "Cereja"):
    print("O quilo da cereja é R$58,00")
elif(fruta == "Banana"):
    print("O quilo da banana é R$5,23")
elif(fruta == "Maça"):
    print("O quilo da maça é R$12,10")
else:
    print(f"Desculpe mas não temos {fruta}")


