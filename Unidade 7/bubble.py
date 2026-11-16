numeros = []

# Solicita 10 números inteiros
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Algoritmo Bubble Sort
for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            aux = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = aux

# Exibe a lista ordenada
print("Números em ordem crescente:")
print(numeros)