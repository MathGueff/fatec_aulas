#Padrâmetro **kwargs
def cores_favoritas(**kwargs):
    for nome in kwargs:
        print(f"{nome} gosta da cor {kwargs[nome]}")
print("1-----------")
cores_favoritas(ana="vermelho", marcelo="amarelo")
print("2-----------")
cores_favoritas(ana="vermelho", marcelo="amarelo", fernanda="branco", matheus="azul")
