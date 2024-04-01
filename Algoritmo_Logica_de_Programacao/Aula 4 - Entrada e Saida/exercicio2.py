# Calculando o salário de um nobre trabalhador

salario = float(input("Diga me o seu salário meu nobre: "))
aumento = float(input("Me diga o percentual de aumento: "))

novo_salario = salario * (1+aumento/100)
print("=====================")
print(f"O seu salário era R${salario:.2f}, com um aumento de {aumento}%, agora o seu salário é R${novo_salario:.2f}")

# APRENDEMOS COISA NOVAAAAAAAAAA
# Se for formatar o limite do número, após usar o "f" antes do conteudo do print, nas chaves onde esta a variavel, colocamos x.yf, onde x é o numero total de casas, incluindo a virgula, e y é a quant de casas apos a virgula, e "f" é format

# Agora ele deixou formatado como se fosse uma conta:

print(f"Salário antigo:.......{salario:8.2f}")
print(f"Aumento:.............{aumento:8.2f}")
print("_____________________________________")
print(f"Salário atual:.......{novo_salario:8.2f}")