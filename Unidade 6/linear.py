numeros = [5, 12, 8, 20, 3, 15, 9, 30, 7, 10]

busca = int(input("Digite um número para procurar: "))

encontrado = False

for numero in numeros:
    if numero == busca:
        encontrado = True
        break

if encontrado:
    print("Número encontrado na lista!")
else:
    print("Número não encontrado!")