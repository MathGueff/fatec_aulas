numero = int(input("Digite um número: "))

divisivel_cinco = numero%5==0
divisivel_tres = numero%3==0

if(divisivel_tres and divisivel_cinco):
    print(f"O número {numero} é divisível por cinco e por três!")
else:
    print(f"O número {numero} não é divisível por cinco e por três")
