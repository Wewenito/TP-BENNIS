liste = []
entier = 0

while len(liste) != 10:
    
    entier = int(input("Veuillez entrer un nombre : "))
    
    if entier < 0 or entier > 20:
        
        entier = int(input("Le nombre doit être compris entre 0 et 20 : "))
        
    else:
        
        liste.append(entier)

val10 = 0
val10à15 = 0
valsupà15 = 0

for x in (liste):
    
    if x < 10:
        
        val10 += 1
        
    elif x >= 10 and x < 15:
        
        val10à15 += 1
        
    elif x >= 15:
        
        valsupà15  += 1
print("\n")
print("Il y a ", val10, "valeurs qui sont inférieurs à 10.")

print("Il y a ", val10à15, "valeurs qui sont supérieurs ou égale à 10 et inférieurs à 15.")

print("Il y a ", valsupà15 , "valeurs qui sont supérieurs ou égale à 15.")
