numeros = [
    2, 4, 6, 8, 10,
    12, 14, 16, 18, 20,
    22, 24, 26, 28, 30,
    32, 34, 36, 38, 40
]

busca = int(input("Digite o número que deseja procurar: "))

# BUSCA LINEAR
comparacoes_linear = 0
encontrado_linear = False

for numero in numeros:
    comparacoes_linear += 1

    if numero == busca:
        encontrado_linear = True
        break

# BUSCA BINÁRIA
inicio = 0
fim = len(numeros) - 1
comparacoes_binaria = 0
encontrado_binaria = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    comparacoes_binaria += 1

    if numeros[meio] == busca:
        encontrado_binaria = True
        break

    elif busca > numeros[meio]:
        inicio = meio + 1

    else:
        fim = meio - 1

# RESULTADOS
print("\n--- RESULTADO ---")

print("Busca linear:")
print("Encontrado:", encontrado_linear)
print("Comparações:", comparacoes_linear)

print("\nBusca binária:")
print("Encontrado:", encontrado_binaria)
print("Comparações:", comparacoes_binaria)