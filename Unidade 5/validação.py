soma = 0
quantidade = 0

for i in range(1, 11):
    nota = float(input("Digite uma nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida! Será ignorada.")
        continue

    soma = soma + nota
    quantidade = quantidade + 1

if quantidade > 0:
    media = soma / quantidade
    print("Média das notas válidas:", media)
else:
    print("Nenhuma nota válida foi informada.")