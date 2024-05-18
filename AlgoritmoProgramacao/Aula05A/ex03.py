a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if((a+b)>c):
    print("Os lados informados formam um triângulo")
    if (a==b==c):
        print("O triângulo é um triângulo Equilátero")
    elif (a==b or b==c or a==c):
        print("O triângulo é um triângulo Isósceles")
    else:
        print("O triângulo é um triângulo Escaleno")

elif((a+c)>b):
    print("Os lados informados formam um triângulo")
    if (a == b == c):
        print("O triângulo é um triângulo Equilátero")
    elif (a == b or b == c or a == c):
        print("O triângulo é um triângulo Isósceles")
    else:
        print("O triângulo é um triângulo Escaleno")

elif ((b+c)>a):
    print("Os lados informados formam um triângulo")
    if (a == b == c):
        print("O triângulo é um triângulo Equilátero")
    elif (a == b or b == c or a == c):
        print("O triângulo é um triângulo Isósceles")
    else:
        print("O triângulo é um triângulo Escaleno")

else:
    print("Não é um triângulo!!")