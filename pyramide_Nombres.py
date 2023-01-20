height = int(input("Entrez la hauteur de la pyramide : "))
for i in range(1, height+1):
    print(" " * (height-i), end='')
    for j in range(1,i+1):
        print(j, end=' ')
    print()