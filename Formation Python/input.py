n = input("Saisir un nombre entier : ")

# print(type(n)) => toute valeur saisie via la fn input est de type str

square = int(n) * int(n) 
print("Le carré de", n, "vaut", square)

print("Le carré de %s vaut %d" % (n,square))