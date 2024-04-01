"""
comentario em varias linhas (3 aspas)
outra linha
"""

# comentário em uma linha (#)

"""====================Operadores Matemáticos============================="""

print(2+2) # Adição (+)
print(2-2) # Substração (-)
print(2/2) # Divisão (/)
print(2*2) # Multiplicação (*)
print(10%2) # Resto Inteiro (%)
print(4**3) # Exponencial (**)
print(10//3) # Divisão Inteira (//)

print("y = (x + 3*b) / (2*x + c)") # Expressão Matemática linearizada

""" ====================Operadores Relacionais============================="""

print(3 > 5) # como 3 é menor que 5, ele retorna que é falso (false)
print(6 > 5) # como 6 é maior que 5, ele retorna que é verdadeiro (true)
print(10 >= 10) # os números são iguais, então retorna true
print(5 <= 4) # o número não é menor ou igual que o outro, então retorna false
print(3==2) # verifica se o número é igual ao outro (se fosse 3 = 2 seria uma atribuição, como x = 2)

""" ====================Operadores Relacionais============================="""

# and (se x e y forem verdadeiros, resulta em verdadeiro, mas todos precisam ser true)
# or (se x ou y forem verdadeiros, resulta em verdadeiro, apenas um precisa ser true)
# not (nega o status, se for true vira false e vice-versa)

x = int(input("Digite um número e vamos ver se ele satisfaz as condições: "))

if(x > 2 and x < 6):{
        print(x, " é  maior que 2 e menor que 6, satisfez as duas condições (and)")
    }

if(x > 10 or x == 5):{
        print(x, " é  maior que 10 ou é igual a 5, satisfez PELO MENOS UMA condição (or)")
    }
