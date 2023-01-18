MOOOOOOOOOOOOOOOOOOOOTS = str("Aliquam pellentesque nec arcu vitae sodales. Morbi wagon molestie massa, at volutpat felis blandit eu. Mauris mattis felis quis wagon consectetur. Phasellus eleifend risus rhoncus, elementum mi ut, semper quam. Nam hendrerit, erat sit amet vehicula vulputate, urna mauris convallis velit, imperdiet tempus tellus ante sit amet elit. Vestibulum efficitur sed elit quis vehicula. In faucibus in magna a mattis. Nulla rutrum odio odio, ut tempus odio imperdiet et. Donec vitae ante aliquet, tempor mi quis, fermentum velit. Morbi id fringilla lacus. Integer suscipit quam vel justo aliquam faucibus. Ut auctor purus eget placerat interdum. Praesent luctus aliquam felis 0")

for i in range(100):
    Tab = MOOOOOOOOOOOOOOOOOOOOTS.split(" ")


LEN = 0

for i in range(100):
    if Tab[i] != 0:
        LEN += 1
    else:
        print(f"Le tableau possède {LEN} éléments")

print(LEN)

Nb_Voyelle = 0
Nb_Wagon = 0

for i in range(LEN):
    if Tab[i] == 'wagon':
        Nb_Wagon += 1
        print(f"Le mot 'Wagon' apparait a la place No {i} de Tab")
    for x in range(len(Tab[i])):
        if Tab[i][x] == 'a' or Tab[i][x] == 'e' or Tab[i][x] == 'i' or Tab[i][x] == 'o' or Tab[i][x] == 'u' or Tab[i][x] == 'y':
            Nb_Voyelle += 1

print(f"Il y a {Nb_Voyelle} voyelles dans le tableau")