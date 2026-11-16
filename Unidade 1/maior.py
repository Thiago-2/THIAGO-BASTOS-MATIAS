maior = None

print("Digite números inteiros (digite 0 para encerrar e ver o maior número):")

while True:
    try:
        numero = int(input("Digite um número: "))
        
        # Condição de parada: se o usuário digitar 0, o loop é encerrado
        if numero == 0:
            break
            
        # Se for o primeiro número ou maior que o atual guardado, atualiza a variável
        if maior is None or numero > maior:
            maior = numero
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Exibe o resultado final (evitando erro caso nenhum número válido tenha sido digitado)
if maior is not None:
    print(f"\nO maior número informado foi: {maior}")
else:
    print("\nNenhum número foi informado antes do zero.")