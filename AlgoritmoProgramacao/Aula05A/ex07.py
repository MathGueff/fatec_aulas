num_vendido = int(input("Digite o número vendido: "))
tipo_combustivel = input("Qual o tipo vendido: (A/G): ").upper()

if(tipo_combustivel == "A"):
    if(num_vendido < 20):
        desconto = num_vendido * 0.03
        valor = num_vendido * 1.90 - desconto
        print(valor)
    else:
        desconto = num_vendido * 0.05
        valor = num_vendido * 1.90 - desconto
        print(valor)
elif(tipo_combustivel == "G"):
    if (num_vendido < 20):
        desconto = num_vendido * 0.04
        valor = num_vendido * 2.50 - desconto
        print(valor)
    else:
        desconto = num_vendido * 0.06
        valor = num_vendido * 2.50 - desconto
        print(valor)
else:
    print("O tipo inserido não existe!")