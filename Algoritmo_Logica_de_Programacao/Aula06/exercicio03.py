largura = float(input("Digite a largura do aposento (metros): "))
comprimento = float(input("Digite o comprimento do aposento (metros): "))
litros_lata = float(input("Quantos litros (L) tem cada lata de tinta (1L, 3.7L ou 18L): "))
# pé direito (2,80m)
# area da porta => 1,68m²

if(litros_lata == 1 or litros_lata == 3.7 or litros_lata == 18):
    print("-------------------------------------------------------")
    #area_aposento = (largura * comprimento * 2.80) - (0.80 * 2.10) - formula que eu tinha feito
    area_aposento = (2 * largura * 2.80) + (2 * comprimento * 2.80) - (0.80 * 2.10)
    area_latas = litros_lata * 3

    qnt_latas = area_aposento/area_latas #retorna o valor que cada lata de xL pinta de metros quadrados
    resto_divisao_latas = area_aposento//area_latas

    if(qnt_latas>resto_divisao_latas and qnt_latas < resto_divisao_latas + 0.5):
        qnt_latas = round(qnt_latas)+1

    print(f"O aposento tem {area_aposento:.2f}m², cada lata de tinta possui {litros_lata}L, sendo assim, cada lata de tinta pinta {area_latas:.1f}m² ({litros_lata}*3)")
    if(qnt_latas < 2):
        print(f"A quantidade de latas que será necessário para pintar esse aposento é de {round(qnt_latas)} lata de tinta ({area_aposento:.1f}/{area_latas:.1f})")
    else:
        print(f"A quantidade de latas que será necessário para pintar esse aposento é de {round(qnt_latas)} latas de tinta ({area_aposento:.1f}/{area_latas:.1f})")
else:
    print("Quantidade de litro da lata de tinta inválida, informe apenas entre 1L, 3.7L ou 18L")