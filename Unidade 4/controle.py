estoque = int(input("Digite a quantidade inicial do estoque: "))

while estoque > 0:
    retirada = int(input("Quantos produtos deseja retirar? "))

    if retirada <= estoque:
        estoque = estoque - retirada
        print("Retirada realizada!")
        print("Estoque atual:", estoque)
    else:
        print("Quantidade indisponível!")

print("Estoque zerado!")