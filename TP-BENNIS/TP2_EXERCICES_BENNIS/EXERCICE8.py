

I = [2, 3, 0, 1, -10, -2]
x = float(input("Entrez un nombre décimal : "))

if (not x < -10 and x <= -2) or (not x < 2 and  x < 3) or (not x <= 0 and x <= 1):
    print("x appartient à I")
else:
    print("x n'appartient pas à I")
