"""Faça uma função que determine se um ano qualquer, no formato
AAAA, é bissexto.
A função retorna 1 se o ano é bissexto e 0(zero) se não."""

def bissexto(ano):
    if(ano%4 == 0):
        return True
    else:
        return False

a = int(input("Digite um ano: "))
if(bissexto(a)):
    print(f"O ano {a} é bissexto")
else:
    print(f"O ano {a} não é bissexto")
