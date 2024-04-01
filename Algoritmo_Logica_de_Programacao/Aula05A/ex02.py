n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2)/2
aprovacao = "REPROVADO"

print("----------------------")

if(media > 9 and media <= 10):
    conceito = "A"
    aprovacao = "APROVADO"
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Média: {media}")
    print(f"Conceito: {conceito}")
    print(f"Aprovação: {aprovacao}")

elif(media > 7.5 and media <= 9):
    conceito = "B"
    aprovacao = "APROVADO"
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Média: {media}")
    print(f"Conceito: {conceito}")
    print(f"Aprovação: {aprovacao}")

elif(media > 6 and media <= 7.5):
    conceito = "C"
    aprovacao = "APROVADO"
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Média: {media}")
    print(f"Conceito: {conceito}")
    print(f"Aprovação: {aprovacao}")

elif(media > 4 and media <= 6):
    conceito = "D"
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Média: {media}")
    print(f"Conceito: {conceito}")
    print(f"Aprovação: {aprovacao}")

else:
    conceito = "E"
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Média: {media}")
    print(f"Conceito: {conceito}")
    print(f"Aprovação: {aprovacao}")
