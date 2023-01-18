x = int(input(" Merci de saisir un nombre supérieur à 1 : "))
som = 0
indice = 0

while indice < x:
    som=som+1
    indice=indice+som
    
    if indice != x:
        print("ceci n'est pas possible")
    else:
        print(som)
    