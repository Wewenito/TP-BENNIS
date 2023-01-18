Verif1 = str(input("Nom fichier1 à verif"))
Verif2 = str(input("Nom fichier2 à verif"))

import os.path

if os.path.isfile(Verif1) == True:
    print("Fichier No 1 existe")
    print(os.path.getmtime(Verif1))
else:
    print("Fichier No 2 n'existe pas")

if os.path.isfile(Verif2) == True:
    print("Fichier No 2 existe")
    print(os.path.getmtime(Verif2)) 
else:
    print("Fichier No 2 n'existe pas")