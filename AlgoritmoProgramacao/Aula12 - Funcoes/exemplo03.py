from math import pi, pow
def area_circulo(raio):
    area = pi*pow(raio,2)
    return area

r = float(input("Digite o valor do raio do círculo: "))
print(f"O valor da área do círculo é: {area_circulo(r)}")