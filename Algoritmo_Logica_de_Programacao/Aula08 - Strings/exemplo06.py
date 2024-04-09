contador = 1

while True:
    idade = input("Digite sua idade: ")
    if idade.isdigit():
        idade = int(idade)
        print("Boa, você não colocou caracteres")
        print(f"De acordo com meus cálculos, você tem {idade} anos")
        break
    else:
        print("Eita doido, coloca só número!")
        print("=================")
        print(contador)
    contador = contador + 1
