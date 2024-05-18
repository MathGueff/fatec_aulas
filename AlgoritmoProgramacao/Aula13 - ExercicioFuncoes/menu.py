from funcoes import *
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            exibir_mensagem()
        elif opcao == '3':
            print("Bye Bye!")
            break
        else:
            print("Opção inválida!")

main()