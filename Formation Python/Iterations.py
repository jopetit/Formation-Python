# Boucles

# print("Bonjour")
# print("Bonjour")
# print("Bonjour")
# print("Bonjour")
# print("Bonjour")

counter = 1
maxiteration = 6
while counter < maxiteration:
    print("Bonjour", counter , "fois")
    counter += 1 # incrémentation, équivalent à counter = counter +1

# print("Au revoir")
counter2 = 5
while counter2 >0:
    print("Au revoir")
    counter2 -= 1 #décrémentation, équivalent à counter = counter -1

# boucle for ... in
# boucle adaptée au parcourt de collection de données
# range renvoye ici à un ensemble de 5 éléments
for i in range(5):
    print(i)
