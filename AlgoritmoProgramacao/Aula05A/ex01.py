valor_hora = float(input("Digite o salário: "))
qnt_h = int(input("Digite a quantidade de horas trabalhadas: "))


salario_bruto = valor_hora * qnt_h
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.10

print("====================================================")
if(salario_bruto <= 900):
    ir = 0.00
    print(f"Salário Bruto: ({qnt_h} * {valor_hora}): R${salario_bruto:.2f}")
    print(f"(-) IR (isento): R${ir:.2f}")
    print(f"(-) INSS (10%): R${inss:.2f}")
    print(f"FGTS (11%): R${fgts:.2f}")
    total_desconto = inss + ir
    print(f"Total de Descontos: R${total_desconto:.2f}")
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Líquido: R${salario_liquido:.2f}")

elif(salario_bruto <= 1500):
    ir = salario_bruto * 0.05
    print(f"Salário Bruto: ({qnt_h} * {valor_hora}): R${salario_bruto:.2f}")
    print(f"(-) IR (isento): R${ir:.2f}")
    print(f"(-) INSS (10%): R${inss:.2f}")
    print(f"FGTS (11%): R${fgts:.2f}")
    total_desconto = inss + ir
    print(f"Total de Descontos: R${total_desconto:.2f}")
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Líquido: R${salario_liquido:.2f}")

elif(salario_bruto <= 2500):
    ir = salario_bruto * 0.10
    print(f"Salário Bruto: ({qnt_h} * {valor_hora}): R${salario_bruto:.2f}")
    print(f"(-) IR (isento): R${ir:.2f}")
    print(f"(-) INSS (10%): R${inss:.2f}")
    print(f"FGTS (11%): R${fgts:.2f}")
    total_desconto = inss + ir
    print(f"Total de Descontos: R${total_desconto:.2f}")
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Líquido: R${salario_liquido:.2f}")

else:
    ir = salario_bruto * 0.20
    print(f"Salário Bruto: ({qnt_h} * {valor_hora}): R${salario_bruto:.2f}")
    print(f"(-) IR (isento): R${ir:.2f}")
    print(f"(-) INSS (10%): R${inss:.2f}")
    print(f"FGTS (11%): R${fgts:.2f}")
    total_desconto = inss + ir
    print(f"Total de Descontos: R${total_desconto:.2f}")
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Líquido: R${salario_liquido:.2f}")
