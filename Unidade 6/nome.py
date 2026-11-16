alunos = [
    "Ana", "Carlos", "Mariana", "Pedro", "João",
    "Beatriz", "Lucas", "Amanda", "Paulo", "Julia"
]

nome_busca = input("Digite o nome do aluno: ")

encontrado = False

for aluno in alunos:
    if aluno.lower() == nome_busca.lower():
        encontrado = True
        break

if encontrado:
    print("Aluno cadastrado!")
else:
    print("Aluno não cadastrado!")