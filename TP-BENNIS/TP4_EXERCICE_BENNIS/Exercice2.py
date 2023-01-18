nbr_stu = int(input("Donnez le nombre d'étudiants : "))
total = 0
notes_stu = []
for i in range(nbr_stu):
    note = float(input("Note étudiant {} : ".format(i)))
    notes_stu.append(note)
    total += note

class_average = total / nbr_stu
print(f"Moyenne de classe : {class_average}")
print(f"Numéro de l'étudiant | note | ecart a la moyenne")
for i in range(nbr_stu):
    note = notes_stu[i]
    ecart = note - class_average
    print(f" {i} | {note} | {ecart}")