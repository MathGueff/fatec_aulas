a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("É um triângulo!")
    if (a==b==c):
        print("é um triângulo Equilátero")
    elif (a==b or b==c or a==c):
        print("É um triângulo Isósceles")
    else:
        print("É um triângulo Escaleno")
else:
    print("Não é um triângulo!!")

