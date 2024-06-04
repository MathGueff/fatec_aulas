with open("entrada.txt", "r", encoding="utf-8") as entrada:
    linhas = entrada.readlines()

espaco_consumido = []
usuarios = []
espaco_total = 0

for li in linhas:
    campos = li.split()
    nome = campos[0] #Nome da pessoa
    bits = int(campos[1]) #Bits usados
    usuarios.append(nome)
    espaco_consumido.append(bits)
    espaco_total += bits

for i in range(0, len(usuarios)):
    espacoMB = espaco_consumido[i] / (1024.0) * (1024.0)
    percent = espaco_consumido[i]/espaco_total * 100
    print(f"{i+1:2d} - {usuarios[i]:11s} - {espaco_consumido[i]:13.2f}MB - {percent:7.2f}%")

print(f"Espaço total ocupado = {espaco_total:.2f}MB")
print(f"Espaço médio ocupado = {espaco_total/len(usuarios):.2f}MB")