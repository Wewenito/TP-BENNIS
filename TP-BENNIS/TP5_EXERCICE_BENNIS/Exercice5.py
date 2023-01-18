Salaire_normal = 160
Max_25 = 200
paie = 0

Nbr_heures = float(input("Combien d'heures travaillées ? \n"))
tarif_horaire = float(input("Combien par heure ? \n"))


if Nbr_heures > Max_25:
    paie = paie + ((Nbr_heures - 200) * (tarif_horaire * 1.5))
    Nbr_heures = Nbr_heures -200

if Nbr_heures > Salaire_normal:
    paie = paie + ((Nbr_heures - 200) * (tarif_horaire * 1.25))
    Nbr_heures = Nbr_heures - Salaire_normal

if Nbr_heures < Salaire_normal:
    paie = paie + (Nbr_heures * tarif_horaire)

print(f"Votre salaire est de : {paie}")