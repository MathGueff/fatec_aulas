from math import pi
def esfera(raio):
    v = 4/3*pi*pow(raio,3)
    return v

r = int(input("Digite o valor do raio: "))
print(f"Volume: {esfera(r)}")

