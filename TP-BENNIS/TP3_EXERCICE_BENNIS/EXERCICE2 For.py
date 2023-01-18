import time

entier = 0
while entier <= 0: 
    entier = int(input("Veuillez entrer un nombre positif : "))
for x in range(0,entier+1):
    print(entier)
    entier -= 1
    time.sleep(1)