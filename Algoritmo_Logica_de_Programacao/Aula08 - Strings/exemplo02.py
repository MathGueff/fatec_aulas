nome = input("Digite seu nome: ")
print(f"Boa noite {nome} !")
print(f"{nome} seja bem-vindo ao curso de Algoritmos...")
print(f"A variável é do tipo string: {type(nome)}")

if nome.lower() == "bruno":
    for i in range(1,8):
        if i == 7:
            print("--------")
            print(f"BOA NOITE {nome}")
        else:
            print("--------")
            print(f"Boa noite {nome}")

# Verificando se é do tipo string