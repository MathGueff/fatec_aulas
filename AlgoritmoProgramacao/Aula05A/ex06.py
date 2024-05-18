num = int(input("Digite um número menor que 1000: "))
if(num < 1000):
    centena = num//100
    dezena = num//10 - centena * 10
    unidade = num - (centena * 10 + dezena) * 10

    if(dezena>0):
        verif_dezena = "true"
    else:
        verif_dezena = "false"

    if(centena > 1):
        centena = str(centena)
        centena = centena + " centenas"
    elif(centena == 1):
        centena = str(centena)
        centena = centena + " centena"

    if (dezena > 1):
        dezena = str(dezena)
        dezena = dezena + " dezenas"
    elif (dezena == 1):
        dezena = str(dezena)
        dezena = dezena + " dezena"

    if (unidade > 1):
        unidade = str(unidade)
        unidade = unidade + " unidades"
    elif (unidade == 1):
        unidade = str(unidade)
        unidade = unidade + " unidade"

    if(centena == 0 and verif_dezena == "true"):
        print(f"{num} = {dezena} e {unidade}")
    elif(centena == 0 and verif_dezena != "true1"):
        print(f"{num} = {unidade}")
    else:
        print(f"{num} = {centena}, {dezena} e {unidade}")
else:
    print("O número informado não é menor que 1000")