nome = input("Digite seu nome completo: ")
nascimento = input("Digite sua data de nascimento <DD/MM/AAAA>: ")
palavras = nome.split()
data = nascimento.split("/")
pre_nome = palavras[0]
sobrenome = palavras[1]
print(nome)
print(data)
print(f"Olá, {pre_nome}... muito bonito o seu sobrenome: {sobrenome}")
print(f"Você nasceu no dia {data[0]} e no mes {data[1]}, e como se não bastasse, no ano {data[2]}")