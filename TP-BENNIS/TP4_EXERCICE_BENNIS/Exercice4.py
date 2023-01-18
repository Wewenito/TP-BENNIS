L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6, 6]


def most_frequent(ARR):
    # Initialize variables to store the most frequent element and its frequency
    Element_Cherché = None
    Nbr = 0
    for i in range(len(ARR)):
        el_actu = ARR[i]
        freq_actu = ARR.count(el_actu)

        # Check if the current element is more frequent than the current most frequent element
        if freq_actu > Nbr:
            Nbr = freq_actu
            Element_Cherché = el_actu
    tab = [Element_Cherché, Nbr]
    return tab

#print(f"Le nombre le plus fréquent est le {most_frequent(L1)[0]} qui est répété {most_frequent(L1)[1]} fois..")

from collections import Counter

count = Counter(L1)
el_commun, el_freq = count.most_common(1)[0]
print(f"Le nombre le plus fréquent dans la liste est le : ({el_commun}, {el_freq})")