def calculate_rate(age, years_licensed, accident_count, loyalty_years):
    rate = ""
    if age < 25 and years_licensed > 2:
        if accident_count == 0:
            rate = "orange"
        elif accident_count == 1:
            rate = "rouge"
        else:
            rate = "refusé"
    elif age >= 25 and years_licensed < 2:
        if accident_count == 0:
            rate = "orange"
        elif accident_count == 1:
            rate = "rouge"
        else:
            rate = "refusé"
    elif age >= 25 and years_licensed > 2:
        if accident_count == 0:
            rate = "vert"
        elif accident_count == 1:
            rate = "orange"
        elif accident_count == 2:
            rate = "rouge"
        else:
            rate = "refusé"
    if loyalty_years > 5 and rate != "refusé":
        if rate == "vert":
            rate = "bleu"
        elif rate == "orange":
            rate = "vert"
        elif rate == "rouge":
            rate = "orange"
    return rate

age = int(input("Entrez l'âge du conducteur: "))
years_licensed = int(input("Entrez le nombre d'années où le conducteur a été titulaire du permis: "))
accident_count = int(input("Entrez le nombre d'accidents provoqués par le conducteur: "))
loyalty_years = int(input("Entrez le nombre d'années où le conducteur est client de la compagnie: "))

print("Tarif proposé:", calculate_rate(age, years_licensed, accident_count, loyalty_years))
