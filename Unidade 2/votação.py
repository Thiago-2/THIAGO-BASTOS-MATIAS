voto1 = 0
voto2 = 0
voto3 = 0

voto = -1

while voto != 0:
    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("0 - Encerrar votação")
    voto = int(input("Digite seu voto: "))
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    elif voto == 0:
        print("Votação encerrada!")
    else:
        print("Voto inválido!")
print("\n===== RESULTADO DA VOTAÇÃO =====")
print("Total de votos na opção 1:", voto1)
print("Total de votos na opção 2:", voto2)
print("Total de votos na opção 3:", voto3)