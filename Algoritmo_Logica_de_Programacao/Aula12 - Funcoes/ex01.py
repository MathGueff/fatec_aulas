"""Faça uma função que retorne o valor lógico V (verdadeiro) se o
número inteiro passado por parâmetro for par, e F (falso) se não."""
def epar(n):
    if n%2 == 0:
        return True
    return False

x = int(input("Digite um valor: "))

if(epar(x)):
    print("O valor digitado é par")
else:
    print("O valor digitado é ímpar")