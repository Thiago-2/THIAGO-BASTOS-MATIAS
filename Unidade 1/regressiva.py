# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é válido
if numero < 0:
    print("Por favor, digite um número inteiro positivo!")
else:
    print("Iniciando a contagem regressiva:")
    while numero >= 0:
        print(numero)
        numero -= 1