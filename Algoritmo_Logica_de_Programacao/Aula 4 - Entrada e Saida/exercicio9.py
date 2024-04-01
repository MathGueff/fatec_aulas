parede = float(input("Me diga o tamanho dessa parede: "))
altura_degrau = int(input("E qual a altura de cada degrau? "))
quant_degrau = parede/altura_degrau
unidade_medida = input("Qual a unidade de medida? ")

print(f"Sendo a altura da parede igual a {parede}{unidade_medida} e a altura do degrau sendo {altura_degrau}{unidade_medida}, a quantidade de degraus que será necessário é de {quant_degrau:.2f} degraus")
