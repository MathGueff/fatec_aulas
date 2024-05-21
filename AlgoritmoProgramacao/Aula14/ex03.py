num = input("Digite um número: ")
soma = 0
multiplicacao = 1
multiplicacaoZero = 1
for n in num:
    soma += int(n)
    if(int(n) > 0):
        multiplicacao *= int(n)
    multiplicacaoZero *= int(n)

print(f"A soma de todos os dígitos de {num} é igual a {soma} e a multiplicação é igual a {multiplicacaoZero}")
print(f"Porém, se ignorarmos o dígito 0, temos como resultado da multiplicação: {multiplicacao}")