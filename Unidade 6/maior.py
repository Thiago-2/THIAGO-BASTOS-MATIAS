numeros = [
    12, 45, 8, 90, 23,
    67, 34, 100, 56, 11,
    78, 29, 5, 88, 41,
    63, 19, 72, 95, 30
]

maior = numeros[0]
indice_maior = 0

for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        indice_maior = i

print("Maior valor:", maior)
print("Índice:", indice_maior)