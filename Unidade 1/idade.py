while True:
    try:
        idade = int(input("Digite a idade (entre 0 e 120): "))
        
        # Verifica se a idade está dentro do intervalo válido
        if 0 <= idade <= 120:
            print(f"\nIdade válida aceita: {idade} anos.")
            break # Encerra o loop se a idade for válida
        else:
            print("Erro: A idade deve estar entre 0 e 120. Tente novamente.")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")