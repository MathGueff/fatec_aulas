import math
a = int(input("Digite o valor de a: "))

if(a == 0):
    print("O valor de a não pode ser igual a 0!")
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    delta = pow(b,2) - 4*a*c
    if(delta < 0):
        print("A equação não possui raizes reais")
    elif(delta == 0):
        x = (-b + math.sqrt(delta))/ 2*a
        print(f"A equação possui apenas uma raiz real, sendo ela: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print(f"A equação possui duas raizes reais, sendo elas: {x1:.1f} e {x2:.1f}")

