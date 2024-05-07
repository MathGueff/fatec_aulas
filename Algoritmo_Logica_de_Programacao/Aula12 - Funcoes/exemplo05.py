"""def soma(n1,n2,n3):
    total = n1+n2+n3
    return total"""

#Escrevemos args por padrão, mas podemos colocar qualquer palavra após o asterisco
def soma(*args):
    """ Args pega todos os valores passados e transforma em uma tupla
    Podemos pegar todos os valores usando um for """
    total = 0
    for i in args:
        total += i
    return total

print(f"Somado: {soma(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)}")
print(help(soma))