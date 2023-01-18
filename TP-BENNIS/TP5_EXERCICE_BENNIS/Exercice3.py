A_tester = str(input("Entrez la phrase a tester : \n"))
t2=""

for i in range (len(A_tester)):
    if A_tester[i].isalpha():
        t2+=A_tester[i]

print(f"String corrigé = {t2}")
t2 = t2.lower()

if (len(t2) % 2) == 0:
    for x in range(int(len(t2) / 2)):
        print(x)
        if t2[x] != t2[(len(t2)-x)-1]:
            print("LA CHAINE N'EST PAS UN PALYNDROME !")
            break
        else:
            print("La chaine est un palyndrome !")
else:
    for x in range(int(len(t2) / 2)):
        if x == len(t2) -x:
            print("La chaine est un palyndrome !")
            break
        if t2[x] != t2[(len(t2)-x)-1]:
            print("LA CHAINE N'EST PAS UN PALYNDROME !")
            break