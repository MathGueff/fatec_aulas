soma = 0
idade = 100
qtd = 0
print("Digite 0 para parar de informar a idade")
print("=================")
while idade != 0:
    idade = int(input(f"Digite a idade {qtd+1}: "))
    if(idade != 0):
        soma = soma + idade
        qtd = qtd + 1

if(qtd == 0):
    print("Nenhuma idade acima de 0 foi informada!")
else:
    media = soma/qtd
    print(f"A média das idades é {round(media):5.2f} anos")
