from datetime import datetime

def VERIF_DATE(input_date):
    try:
        date = datetime.strptime(input_date, "%d%m%Y")
        if date > datetime.now():
            raise ValueError("/!\ DATE INVALIDE /!\ : La date est dans le futur")
        return True
    except ValueError as e:
        print(str(e))
        return False
    except:
        print("/!\ DATE INVALIDE /!\. Veuillez entrez la date au format 'jjmmaaaa'.")
        return False
date_input = input("Selectionner un date sous le format : 'jjmmaaaa': ")
if VERIF_DATE(date_input):
        print(f"La date {date_input} est valide.")
else:
    print(f"/!\ La date {date_input} est invalide. /!\ ")