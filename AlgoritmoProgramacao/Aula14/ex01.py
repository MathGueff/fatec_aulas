"""def patoCoelho(cabeca, pes):
    qtdCoelhos = 0
    qtdPatos = 0
    pCoelho = 4
    pPato = 2
    totalPes = 0

    #21 pés
    # 6 cabeças
    subPes = 0
    if(pes%pCoelho != 0):
        while pes%pCoelho != 0:
            pes -= 1
            subPes += 1
        qtdCoelhos = pes/pCoelho
        if(subPes/pPato < 1):
            qtdPatos = 0
        else:
            qtdPatos = subPes/pPato
    else:
        qtdCoelhos = pes/pCoelho

    return qtdCoelhos, qtdPatos"""

"""def patoCoelho(cabeca, pes):
    tPatos = 0
    tCoelhos = 0

    pCoelhos = 4 #pes por coelho
    pPatos = 2 #pes por coelho
    res = -1
    patas = 0 #Quantidade somatória de patas

    while res != pes:
        for i in range(cabeca):
            if(patas < pes):
                patas += pCoelhos
                tCoelhos += 1
                patas += pPatos
                tPatos += 1
            elif(patas > pes):
                if((patas - 2) >= pes):
                    tPatos -= 1
                else:
                    tCoelhos -= 1
                while patas > pes:
                    patas -= 1
        res = tCoelhos * pCoelhos + tPatos * pPatos
        return tPatos, tCoelhos"""

def patoCoelho(cabeca, pes):
    tPato = 0
    tCoelho = 0

    pes = tPato*2 + tCoelho*4
    cabeca = tPato + tCoelho

    return tPato, tCoelho

cab = int(input("Digite a quantidade de cabeças: "))
pe = int(input("Digite a quantidade de patas: "))
if(patoCoelho(cab,pe)[0] + patoCoelho(cab,pe)[1] < pe):
    print(f"O total de patos é {patoCoelho(cab,pe)[1]} e o total de coelhos é {patoCoelho(cab, pe)[0]}, porém, parece que um patinho perdeu um dos seus pés... então temos {patoCoelho(cab,pe)[1]+ 0.5} patos!")