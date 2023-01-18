import time

entier = 0
while entier <= 0:
    entier = int(input("Veuillez saisir un nombre positif : "))
while entier != -1:
    print(entier)
    entier -= 1
    time.sleep(1)