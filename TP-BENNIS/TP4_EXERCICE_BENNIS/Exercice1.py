def table_multi(n):
    table = []
    for i in range(1, 10):
        result = n*i
        table.append(f"{n} * {i} = {round(result, 2)}")
    print(f"Voici la table de multiplication de {n}")
    for i in range(0,9):
        print(table[i])

nombre = float(input("Entrez le nombre dont vous souhaitez connaitre la table :\n"))


table_multi(nombre)