from funcoes import segundos

"""Crie uma função que receba como parâmetro 3 números interios
(representando horas, minutos e segundos). A função deve
converter em segundos"""

hora = int(input("Digite as horas: "))
minuto = int(input("Digite os minutos: "))
segundo = int(input("Digite os segundos: "))

print(f"O tempo digitado {hora} hora(s),{minuto} minuto(s), {segundo} segundo(s) equivalem a {segundos(hora,minuto,segundo)} segundos")