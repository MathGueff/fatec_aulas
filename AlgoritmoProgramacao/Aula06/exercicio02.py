valor_compra = float(input("Digite o valor da compra: "))

print("---------------------------")
if(valor_compra<=1000):
    desconto = 0.10
    valor_descontado = valor_compra*(1-desconto)
    valor_desconto = valor_compra * desconto
    print(f"Valor da compra: R${valor_compra:.2f}")
    print(f"Desconto (10%): R${valor_desconto:.2f}")
    print(f"Valor com o desconto: R${valor_descontado:.2f}")
elif(5000>=valor_compra>=1001):
    desconto = 0.20
    valor_descontado = valor_compra * (1 - desconto)
    valor_desconto = valor_compra * desconto
    print(f"Valor da compra: R${valor_compra:.2f}")
    print(f"Desconto (20%): R${valor_desconto:.2f}")
    print(f"Valor com o desconto: R${valor_descontado:.2f}")
else:
    desconto = 0.30
    valor_descontado = valor_compra * (1 - desconto)
    valor_desconto = valor_compra * desconto
    print(f"Valor da compra: R${valor_compra:.2f}")
    print(f"Desconto (30%): R${valor_desconto:.2f}")
    print(f"Valor com o desconto: R${valor_descontado:.2f}")

print("---------------------------")