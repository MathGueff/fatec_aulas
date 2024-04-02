import math

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número (pode ser o mesmo também): "))

divisao = n1/n2
divisao_inteira = n1//n2

print(f"A divisão inteira é: {divisao_inteira}")
print(f"A divisão arredondada é: {round(divisao)}")
print(f"A divisão sem arredondamento é: {divisao}")
print(f"Testando: {math.ceil(divisao)}")

print("------")
if(divisao>divisao_inteira and divisao < divisao_inteira +0.5):
    divisao = round(divisao)+1
    print(f"Precisei fazer toda essa maracutaia, agora o valor é: {divisao}")
else:
    print(f"Sem problemas, o arredondamento já funcionou, e deu: {round(divisao)}")

    #O math.ceil faz tudo isso que eu fiz :D