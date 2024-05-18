from math import pow
def potencia(base,expoente=2):
    """ Função que calcula a potencia de um número.
    Valor de Entrada:
    base = base a ser calculado (elevado a potencia) (float)
    expoente = expoente utilizado no cálculo (inteiro)
    Resultado:
    Resultado do cálculo (float)"""
    resultado = pow(base,expoente)
    return resultado

b = int(input("Digite o valor da base: "))
e = int(input("Digite o expoente: "))

print("========")

print(f"O valor com expoente: {potencia(b,e)}")
print(f"O valor sem o expoente (padrão 2): {potencia(b)}")
print(f"O valor com expoente e base trocados de ordem (mesmo resultado): {potencia(expoente=e,base=b)}")
#DocString
print(help(len))