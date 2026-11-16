# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro para ver a tabuada: "))

contador = 1

print(f"\nTabuada do {numero}:")
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1