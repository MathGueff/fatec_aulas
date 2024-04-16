from random import randint
total = 30000
resultado = [0]*11
# [2,3,4,5,6,7,8,9,10,11,12] -> 11 posições
print(resultado)
for i in range(total):
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print(dado1)
    print(dado2)
    soma = dado1 + dado2
    print(soma)
    resultado[soma-2] = resultado[soma-2] + 1
    print(resultado)
    print("------")

for i in range(11):
    print(f"{i+2} - frequência: {resultado[i]/total*100:.2f}%")

if(round(resultado[5]/30000*100) == round(1/6*100)):
    print("A frequência de somas iguais a 7 é igual a 1/6")
else:
    print("Não foi dessa vez")
    print(round(resultado[5]/30000*100))
    print(round(1/6*100))