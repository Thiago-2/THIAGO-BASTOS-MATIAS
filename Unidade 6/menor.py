numeros = [
    12, 45, 8, 90, 23,
    67, 34, 100, 56, 11,
    78, 29, 5, 88, 41,
    63, 19, 72, 95, 30
]

menor = numeros[0]
indice_menor = 0

for i in range(len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]
        indice_menor = i

print("Menor valor:", menor)
print("Índice:", indice_menor)