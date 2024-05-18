data = input("Digite uma data: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6::]
print(ano+ "/" + mes + "/" + dia) # Usando substr

data_formatada = data.split("/")
print(data_formatada[2] + "/" + data_formatada[1] + "/" + data_formatada[0]) # Usando Split


# Alterando formato da data usando o split e substr