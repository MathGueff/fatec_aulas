from datetime import datetime
import random
#validação CPF

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif1 = 0
    else:
        digito_verif1 = 11 - resto

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif2 = 0
    else:
        digito_verif2 = 11 - resto

    if int(cpf[9]) == digito_verif1 and int(cpf[10]) == digito_verif2:
        return True
    else:
        return False

def valida_data(data):
    #if len(data) == 8:
    data = data.split("/")
    if (len(data) == 3):
        a = int(data[2])
        m = int(data[1])
        d = int(data[0])
    else:
        return False
    if(d <= 31 and m <= 12):
        hoje = datetime.now().date()
        data_nasc = datetime(a, m, d).date()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        if(idade >= 18):
            return True
        else:
            return False
    else:
        return False
def exibir_menu():
    print('Tecle:')
    print('1 - Cadastrar')
    print('2 - Exibir Mensagem')
    print('3 - Sair')
def cadastrar():
    nome = input("Digite o seu primeiro nome: ")
    sobrneome = input("Digite o seu sobrenome: ")
    cpf = input("Digite o seu CPF: ")
    while valida_cpf(cpf) == False:
        print("CPF Inválido!")
        cpf = input("Digite o número do CPF: ")
    data = input("Digite sua data de nascimento (DD/MM/AAAA)")
    while valida_data(data) == False:
        print("Data Inválida! ")
        data = input("Digite a data de nascimento: (formato: DD/MM/AAAA) ")
    renda_bruta = float(input("Digite sua renda bruta: "))
    print("Usuário cadastrado com sucesso!")
def exibir_mensagem():
    frase = [
    "A persistência realiza o impossível",
    "Seus sonhos não precisam de plateia, eles só precisam de você",
    "A persistência é o caminho do êxito",
    "No meio da dificuldade encontra-se a oportunidade"
    ]
    print(random.choice(frase))
