soma = 0
quantidade = 0

print("Digite as notas dos alunos (digite -1 para encerrar e ver a média):")

while True:
    try:
        nota = float(input("Digite a nota (0 a 10): "))
        
        # Condição de parada
        if nota == -1:
            break
            
        # Validação da nota (entre 0 e 10)
        if 0 <= nota <= 10:
            soma += nota
            quantidade += 1
        else:
            print("Nota inválida! Digite um valor entre 0 e 10 (ou -1 para sair).")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Cálculo e exibição da média (evitando divisão por zero)
if quantidade > 0:
    media = soma / quantidade
    print(f"\nForam contabilizadas {quantidade} notas válidas.")
    print(f"A média das notas é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi informada.")