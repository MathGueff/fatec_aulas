def isPrimo(n):
    if(n>2):
        for i in range(2,n):
            if(n%i == 0):
                return False
        return True
    else:
        return False

def qtdPrimos(fim):
    qtd = 0
    soma = 0
    i = 0
    listaNumeros = []
    while qtd < fim:
        if(isPrimo(i)):
            qtd += 1
            listaNumeros.append(i)
        i += 1

    if(qtd == fim):
        for num in range(len(listaNumeros)):
            soma += listaNumeros[num]
    print(listaNumeros)
    return soma

numero = int(input("Digite um número: "))
print(f"A soma dos {numero} primeiros números primos dá: {qtdPrimos(numero)}")

# Dois últimos dígitos do meu RA -> 06
# y = 6
# 6*2+5 = 17 primeiros numeros primos
