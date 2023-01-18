n = int(input("Entrez un nombre entier : "))

if n > 0:
    if (n % 2) == 0:
       print("Le nombre est positif & pair".format(n))
    if (n % 2) == 1:
       print("Le nombre est positif & impair".format(n))
 
if n <0:
    if (n % 2) == 0:
       print("Le nombre est négatif & pair".format(n))
    if (n % 2) == 1:
       print("Le nombre est négatif & impair".format(n))

if n == 0:
        print("Le nombre est zéro, donc pair".format(n))