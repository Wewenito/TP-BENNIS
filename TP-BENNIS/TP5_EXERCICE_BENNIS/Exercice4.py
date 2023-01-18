cent = 0
cinquante = 0
dix = 0
deux = 0
un = 0

val = int(input("Entrez la valeur a compter : \n"))

start_input = val

while val != 0:
    for i in range(10):
        if (val - 100) >= 0:
            val = val - 100
            cent = cent + 1
        else:
            break
    for x in range(10):
        if (val - 50) >= 0:
            val = val - 50
            cinquante = cinquante + 1
        else:
            break
    for y in range(10):
        if (val - 10) >= 0:
            val = val -10
            dix = dix + 1
        else:
            break
    for z in range(10):
        if (val - 2) >= 0:
            val = val -2
            deux = deux + 1
        else:
            break
    for t in range(10):
        if (val - 1) >= 0:
            val = val -1
            un = un + 1
        else:
            break


print(f"La valeur {start_input} est composée de : \n- {cent} Billets de 100\n- {cinquante} Billets de 50\n- {dix} Billets de 10\n- {deux} Pièces de 2\n- {un} Pièces de 1\n")