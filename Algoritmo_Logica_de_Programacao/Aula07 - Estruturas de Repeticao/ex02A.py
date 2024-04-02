calc_altura = 0
calc_peso = 0
maior_imc = 0
menor_imc = 100

for i in range (1,6):
    peso = float(input("Digite seu peso (KG): "))
    altura = float(input("Digite sua altura (M): "))

    imc = peso / altura ** 2

    if (imc < 24):
        print(f"Seu IMC é {imc:.2f}, classificado como: perda de peso")
    elif (imc == 24):
        print(f"Seu IMC é {imc:.2f}, classificado como: peso ideal")
    elif (imc > 24):
        print(f"Seu IMC é {imc:.2f}, classificado como: sobrepeso")
    elif (imc > 32):
        print(f"Seu IMC é {imc:.2f}, classificado como: obesidade")

    if(i < 5):
        print("---------------------")



    if(imc > maior_imc):
        maior_imc = imc

    if(imc < menor_imc):
        menor_imc = imc

    calc_peso = calc_peso + peso
    calc_altura = calc_altura + altura

media_peso = calc_peso/5
media_altura = calc_altura/5

print("---------------------")
print(f"Maior IMC: {maior_imc:.2f}")
print(f"Menor IMC: {menor_imc:.2f}")
print(f"A média dos pesos é {media_peso:.2f}")
print(f"A média das alturas é {media_altura:.2f}")
