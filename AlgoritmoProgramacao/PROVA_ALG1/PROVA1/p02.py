pop_a = 80000
pop_b = 200000
taxa_a = 1.3
taxa_b = 1.15
cont_anos = 0

print(f"População A inicial: {pop_a}")
print(f"População B inicial: {pop_b}")
print("=====")
while pop_a <= pop_b:
    pop_a = pop_a * taxa_a
    pop_b = pop_b * taxa_b
    cont_anos += 1
    if (cont_anos == 1):
        print(f"{cont_anos} ano se passou")
    else:
        print(f"{cont_anos} anos se passaram")
    print(f"População A atual: {int(pop_a)}")
    print(f"População B atual: {int(pop_b)}")
    print("=====")

if(cont_anos == 1):
    print(f"Foi necessário {cont_anos} ano até a população A({int(pop_a)} habitantes) passar ou se igualar a população B({int(pop_b)} habitantes)")
else:
    if(pop_a == pop_b):
        print(f"Foram necessários {cont_anos} anos até a população A({int(pop_a)} habitantes) se igualar a população B({int(pop_b)} habitantes)")
    else:
        print(f"Foram necessários {cont_anos} anos até a população A({int(pop_a)} habitantes) passar a população B({int(pop_b)} habitantes)")
