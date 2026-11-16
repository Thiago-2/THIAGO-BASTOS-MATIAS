opcao = 0

while opcao != 4:
    print("\n===== MENU =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 + n2)

    elif opcao == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 - n2)

    elif opcao == 3:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 * n2)

    elif opcao == 4:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")