from random import randint
m = []
l = []

for y in range(4): #Cria cada linha
    for x in range(4): #Preenche cada linha
        l.append(randint(1, 100))
    m.append(l)
    l = []

soma = 0
for i in range(4):
    soma = soma + m[i][i]

print(f"""A soma da diagonal principal é {soma}, sendo que:
[0,0]= {m[0][0]} 
[1,1]= {m[1][1]}
[2,2]= {m[2][2]} 
[3,3]= {m[3][3]}""")