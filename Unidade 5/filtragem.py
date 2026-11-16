nomes = [
    "Ana", "Carlos", "Amanda", "Pedro", "Alice",
    "João", "Bruna", "Arthur", "Mariana", "André"
]

for nome in nomes:

    if nome.upper().startswith("A"):
        continue

    print(nome)