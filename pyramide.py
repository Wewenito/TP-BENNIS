def TakeInput():
    n = int(input("Taille souhaitée de la pyramide (Nbr de ligne): "))
    y = str(input("\nVous la voulez à l'endroit ou à l'envers ? : (UP/DOWN)"))
    if n > 50:
        print("Input invalide, taille max 50")
        TakeInput()
    if y == "UP" or y == "up":
        for i in range(1, n+1):
            print(" "*(n-i) + "*"*(2*i-1))
    if y == "DOWN" or y == "down":
        for i in range(n, 0, -1):
            print(" "*(n-i) + "*"*(2*i-1))

TakeInput()







