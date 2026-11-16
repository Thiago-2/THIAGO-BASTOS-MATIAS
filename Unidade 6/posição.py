numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

busca = int(input("Digite um número para procurar: "))

encontrado = False

for i in range(len(numeros)):
    if numeros[i] == busca:
        print("Número encontrado no índice:", i)
        encontrado = True
        break

if encontrado == False:
    print("Número não encontrado!")