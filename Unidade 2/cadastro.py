alunos = []
continuar = "s"
while continuar == "s":
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
print("\nAlunos cadastrados:")
for aluno in alunos:
    print(aluno)
print("Cadastro encerrado!")