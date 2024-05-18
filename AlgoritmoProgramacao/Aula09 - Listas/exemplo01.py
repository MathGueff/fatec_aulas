lista = []
for i in range(10):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)


#Imprimindo ao contrário usando for
for i in range(9,-1,-1):
    print(lista[i], end="") #end faz com que não pulemos linha ao fazer um print!!
    # Posso colocar o que quiser no end, ele vai aparecer depois do valor inserido no print


#Imprimindo ao contrário usando lista.reverse
lista.reverse()
print(lista)