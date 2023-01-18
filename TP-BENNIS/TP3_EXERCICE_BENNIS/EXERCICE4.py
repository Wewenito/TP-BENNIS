nombre = int(input("Veuillez rentrer un nombre : "))
y = nombre
liste = []
factorielle = 1

while nombre != 1:
    liste.append(nombre)
    nombre-=1

question = input("Selection de la boucle (while / for) ?")

if question == "while":
    x = 1
    
while y <= len(liste):
    factorielle = factorielle * x
    x = x + 1
        
if question == "for":
    factorielle = 1
    
for x in range(len(liste)):
    factorielle *= liste[x]

print("La factorielle de", x, "est", factorielle, ".")