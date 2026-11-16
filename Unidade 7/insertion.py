numeros = []

# Solicita 10 números inteiros
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Algoritmo Insertion Sort
for i in range(1, len(numeros)):
    chave = numeros[i]
    j = i - 1

    while j >= 0 and numeros[j] > chave:
        numeros[j + 1] = numeros[j]
        j = j - 1

    numeros[j + 1] = chave

    # Mostra o estado da lista após cada inserção
    print("Após a inserção:", numeros)

print("Lista ordenada:", numeros)