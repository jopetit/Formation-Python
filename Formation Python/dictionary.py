# un dictionnaire est une structure clé/valeur
# permettant de modéliser une information/entité

import separator
import tools as t

t.example()

d ={}
# print (type(d)) # <class 'dict'>

studentTuple = ("Chris", "DUFOUR", 99)

student = {
    "firstname": "Chris",
    "lastname": "DUFOUR",
    "email": "c.dufour@python.com",
    "age": 99,
    "rates": [8,12,17]}

print(student["firstname"], "a", student["age"], "ans")
student["lastname"] = "Dufour"
student["rates"].append(15)
student["tel"] = "0788996633" # ajoute une nouvelle clé
student.pop("age") # supprime la clé
# print(student)

for x in student:
        # affiche la clé et la valeur associée
    print(x, "=>", student[x])

for v in student.values(): # itére uniquement sur les valeurs du dictionnaire
    print(v)

for k in student.keys(): # itère uniquement sur les clés du dictionnaire
    print(k)