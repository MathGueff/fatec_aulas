"""Faça uma função que retorne o valor lógico V (verdadeiro) se o
número inteiro passado por parâmetro for primo, e F (falso) se
não"""
def eprimo(valor):
    cont = 0
    if(valor<2):
        return False
    for i in range(int(valor/2)+1):
        if(valor%(i+1) == 0):
            cont += 1
    if(cont>2):
        return False
    else:
        return True

x = int(input("Digite um valor: "))
if(eprimo(x)):
    print(f"O valor digitado {x} é primo")
else:
    print(f"O valor digitado {x} não é primo")