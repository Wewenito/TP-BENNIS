DICO = {}

DICO['firstname'] = "owen"
DICO['lastname'] = "pichot"
DICO['promo'] = "RT1"
DICO['group'] = "rt122"

print(f"Mon nom est {DICO['firstname']} {DICO['lastname']} de la promo {DICO['promo']} et du groupe {DICO['group']}")
input("CONTINUER \n")

print(f"Les clefs du dico sont :\n-{list(DICO.keys())[0]}\n-{list(DICO.keys())[1]}\n-{list(DICO.keys())[2]}\n-{list(DICO.keys())[3]}")
print(f"Les valeurs du dico sont :\n-{list(DICO.values())[0]}\n-{list(DICO.values())[1]}\n-{list(DICO.values())[2]}\n-{list(DICO.values())[3]}")
print(f"Les Tuplets du dico sont :\n-{list(DICO.items())[0]}\n-{list(DICO.items())[1]}\n-{list(DICO.items())[2]}\n-{list(DICO.items())[3]}")

input("CONTINUER \n")

DICO2 = {}

DICO2['firstname'] = "henry"
DICO2['lastname'] = "budzynski"
DICO2['promo'] = "RT1"
DICO2['group'] = "rt122"

binome = {}

binome['owen'] = DICO
binome['henry'] = DICO2

print(f"Les etudiants formants le binôme sont : \n - L'étudiant {binome['owen']['firstname']} du groupe {binome['owen']['group']} \n - L'étudiant {binome['henry']['firstname']} du groupe {binome['henry']['group']}")

# Les étudiants formants le binôme sont :
# - L'étudiant toto titi du groupe 202
# - L'étudiant tata tutu du groupe 102