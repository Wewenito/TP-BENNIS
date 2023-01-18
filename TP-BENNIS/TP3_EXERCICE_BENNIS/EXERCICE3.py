from random import*

x = randint(0, 100)
y = -1
z = 0

while y != x:
    y = int(input("Entrez le chiffre auquel je pense : "))
    z +=1
    
    if y < x:
        print("Trop petit")
        
    if y > x:
        print("Trop grand")
    
    elif y == x:
        print("GG !")
        
        break

print("Trouver la solution vous aura pris ", z ,"essais.")

    
    
