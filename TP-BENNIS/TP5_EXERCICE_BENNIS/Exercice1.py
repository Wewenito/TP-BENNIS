Prenom1 = str(input("Entrez le prénom de la première personne : \n"))
Nom1 = str(input("Entrez le nom de la première personne : \n"))

Prenom2 = str(input("Entrez le prénom de la seconde personne : \n"))
Nom2 = str(input("Entrez le nom de la seconde personne : \n"))

if Nom1 < Nom2:
    print(str.capitalize(Prenom1), str.upper(Nom1))
    print(str.capitalize(Prenom2), str.upper(Nom2))
if Nom1 == Nom2:
    if Prenom1 < Prenom2:
        print(str.capitalize(Prenom1), str.upper(Nom1))
        print(str.capitalize(Prenom2), str.upper(Nom2))
    else:
        print(str.capitalize(Prenom2), str.upper(Nom2))
        print(str.capitalize(Prenom1), str.upper(Nom1))
else:
    print(str.capitalize(Prenom2), str.upper(Nom2))
    print(str.capitalize(Prenom1), str.upper(Nom1))

