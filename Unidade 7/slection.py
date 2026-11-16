numeros = []

# Solicita 10 números inteiros
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Algoritmo Selection Sort
for i in range(len(numeros)):
    menor = i

    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[menor]:
            menor = j

    # Troca os elementos de posição
    aux = numeros[i]
    numeros[i] = numeros[menor]
    numeros[menor] = aux

# Exibe a lista ordenada
print("Números em ordem crescente:")
print(numeros)