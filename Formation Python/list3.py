from typing import Counter


postCodes = [
    67200, 75012, 68520, 15000, 75020,
    67200, 75012, 68520, 15000, 75020,
    67200, 75012, 68520, 15000, 75020
]

# print(len(postCodes)) affiche la longueur de la liste => 10

# code = 75020
# if code[:2] == 75:
#     print("Paris")

#combien de codes parisiens ?

numParis = 0
for code in postCodes:
    if code >=75000 and code < 76000:
        numParis += 1
print("Nombre de codes postaux parisiens :", numParis, "sur", len(postCodes))


