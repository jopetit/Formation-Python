students = [
    "AFOUDA Pamela",
    "CASTETS Pierre",
    "DEBALS Alexandre",
    "PELLE Pierre-Jean",
    "SAUPAGNA Sébastien"
]

# Objectif : obtenir une adresse mail à partir de la chaîne Nom Prénom
# Exemple : "AFOUDA Pamela" => pamela.afouda@python.com
'''
student = "AFOUDA Pamela" .lower() #mise en base de casse
spaceIndex = student.find(" ")
lastName = student[:spaceIndex] # Nom de famille
firstName = student[spaceIndex + 1:]
email = firstName + "." + lastName + "@" + "python.com"

print(email)
'''

for s in students:
    student = s.lower() #mise en base de casse
    spaceIndex = student.find(" ")
    lastName = student[:spaceIndex] # Nom de famille
    firstName = student[spaceIndex + 1:]
    email = firstName + "." + lastName + "@" + "python.com"
    emailNoAccent = email.replace("é", "e", )
    print(emailNoAccent)
    # exemple de chaînage de méthodes de str
    # print(s.lower().replace("é", "e").replace("-", "_").upper())

