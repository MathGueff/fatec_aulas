# Calcular a distância entre dois pontos


# Para importar da biblioteca, podemos usar "import math" que importa todos os comandos, ou from math import (especificar função)


# import math (precisa usar math.pow se querer usar a função pow)
from math import pow, sqrt

print("Vamos calcular a distância")

x1 = int(input("Digite o valor de x1: "))
x2 = int(input("Digite o valor de x2: "))
dx = x2 - x1

y1 = int(input("Digite o valor de y1: "))
y2 = int(input("Digite o valor de y2: "))
dy = y2 - y1

dz = sqrt(pow(dx, 2)+pow(dy, 2))

print(f"O valor da distância é {dz}")
