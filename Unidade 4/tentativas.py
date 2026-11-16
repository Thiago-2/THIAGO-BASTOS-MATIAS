numero_secreto = 15

tentativa = int(input("Adivinhe o número entre 1 e 20: "))

while tentativa != numero_secreto:

    if tentativa > numero_secreto:
        print("O número secreto é menor!")

    elif tentativa < numero_secreto:
        print("O número secreto é maior!")

    tentativa = int(input("Tente novamente: "))

print("Parabéns! Você acertou!")