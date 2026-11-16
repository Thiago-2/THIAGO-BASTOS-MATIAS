# Solicita um número inteiro não negativo ao usuário
n = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número é válido
if n < 0:
    print("Erro: O fatorial não está definido para números negativos.")
else:
    fatorial = 1
    contador = n
    
    # Cálculo do fatorial usando while (contagem regressiva)
    while contador > 1:
        fatorial *= contador
        contador -= 1
        
    print(f"O fatorial de {n} (representado como {n}!) é: {fatorial}")