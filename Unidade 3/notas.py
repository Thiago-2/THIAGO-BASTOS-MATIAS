soma = 0

for i in range(1, 11):
    nota = float(input("Digite a nota do aluno: "))

    soma = soma + nota

    if i == 1:
        maior = nota
        menor = nota

    else:
        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

media = soma / 10

print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média da turma:", media)