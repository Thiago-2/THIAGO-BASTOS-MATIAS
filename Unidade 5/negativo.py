soma = 0

for i in range(1, 11):
    numero = int(input("Digite um número inteiro: "))

    if numero < 0:
        continue

    soma = soma + numero

print("A soma dos valores não negativos é:", soma)