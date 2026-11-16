numeros = [
    2, 4, 6, 8, 10,
    12, 14, 16, 18, 20,
    22, 24, 26, 28, 30,
    32, 34, 36, 38, 40
]

busca = int(input("Digite o número que deseja procurar: "))

inicio = 0
fim = len(numeros) - 1
encontrado = False

while inicio <= fim:

    meio = (inicio + fim) // 2

    if numeros[meio] == busca:
        print("Número encontrado no índice:", meio)
        encontrado = True
        break

    elif busca > numeros[meio]:
        inicio = meio + 1

    else:
        fim = meio - 1

if encontrado == False:
    print("Número não encontrado!")