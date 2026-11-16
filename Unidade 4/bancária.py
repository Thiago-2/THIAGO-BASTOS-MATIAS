saldo = 0

while True:
    print("\n--- MENU BANCÁRIO ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo = saldo + deposito
            print("Depósito realizado!")
        else:
            print("Valor inválido!")

    elif opcao == 2:
        saque = float(input("Digite o valor do saque: "))
        if saque > 0 and saque <= saldo:
            saldo = saldo - saque
            print("Saque realizado!")
        else:
            print("Saque inválido ou saldo insuficiente!")

    elif opcao == 3:
        print("Saldo atual: R$", saldo)

    elif opcao == 4:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")