soma = 0

print("Digite números inteiros (digite 0 para encerrar e ver a soma):")

while True:
    numero = int(input("Digite um número: "))
    
    # Condição de parada: se o usuário digitar 0, o loop é encerrado
    if numero == 0:
        break
        
    # Acumula o valor na variável soma
    soma += numero

print(f"\nA soma total de todos os números informados é: {soma}")