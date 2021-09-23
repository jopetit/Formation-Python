f = open("files/cities.csv", "r")
content = f.read() # lecture du fichier et stockage de son contenu
f.close ()

rows = content.splitlines()
cityNameIndex = 8
n = 0  # compteur du nombre de ville correspondant aux critères de recherche

for r in rows:
    cols = r.split(",") # virgule, comme séparateur de colonnes
    cityName = cols[cityNameIndex].strip().strip('"') # enléve les espaces de début et fin de chaîne, enlève les guillemets début/fin de chaîne
    # print(cityName, "=>", len(cityName))
    if cityName.startswith("San"):
        n += 1

print("Nombre de villes trouvées : %d" % n)

