dicionario = {}
maior_idade = 0
for i in range(3):
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite sua idade: "))
    print("---")
    dicionario[sobrenome] = idade
    if(dicionario[sobrenome] > maior_idade):
        maior_idade = dicionario[sobrenome]
        pessoa = sobrenome

print(f"A pessoa com a maior idade é {pessoa}, com {maior_idade} anos")