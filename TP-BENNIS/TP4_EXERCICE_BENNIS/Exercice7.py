binome = ('login1', 'login2')

print(binome)

newL = str(input("Entrez le nouveau login souhaité\n"))

binome = list(binome)

binome[1] = newL

binome = tuple(binome)

print(binome)

newL2 = str(input("Entrez le nouveau login a ajouter :\n"))

binome = list(binome)

binome.append(newL2)

binome = tuple(binome)

print(binome)
