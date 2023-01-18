gradesT = []

moyenne = 0.00

for i in range(5):
    grades = str(input("Veuillez entrer la note du module 1 et le coefficient correspondant : \n"))
    gradesT.append(grades)

print(gradesT)

for x in range(0,5):
    Sep = gradesT[x].split(" ")
    Sep[0] = int(Sep[0])
    Sep[1] = int(Sep[1])
    if moyenne == 0.00:
        moyenne = (Sep[0] * Sep[1]) / Sep[1]
    else:
        moyenne = (((Sep[0] * Sep[1]) / Sep[1]) + moyenne) / 2

print(f"Votre moyenne est de : {moyenne}")