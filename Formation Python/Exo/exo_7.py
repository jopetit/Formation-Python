'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")

import csv, operator

lecteur = csv.reader(open("deniro.csv"), delimiter =",")
fileName = "deniro-report.txt"
nbrMovie = 0
movieYears = range(2000,2011)

for year, score, title in lecteur:
    print(sorted(lecteur, key=operator.itemgetter(1), reverse=True))
    
    
    # print(year.strip(), score.strip().strip("\""), title.strip().strip("\""))
