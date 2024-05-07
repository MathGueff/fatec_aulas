def tem_igual(*args):
    for i in range(len(args)-1): #Se tiver 6 numeros, vai até o quinto
        n = args[i] #Pega o valor da posição 0,1,2,3...
        print(n)
        # Começa do próximo do atual, sendo i+1, e termina no último
        for j in range(i+1, len(args)):
            print(f"args[i] = {args[i]} -> ", end="")
            print(f"args[j] = {args[j]}")
            #Faz a verificação se o número é igual aos outros, e repete percorrendo todos os próximos
            if(args[i] == args[j]):
                return True
    return False

print(f"Entre os valores, existe valor igual, a declaração é: {tem_igual(1,2,3,4,5)} ")