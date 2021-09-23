'''
f = open("blabla.txt", "r") # r => lecture
print(f.read())
f.close()

f = open("blabla.txt", "w") # x, a, w => écriture
f.write("Simple fichier texte")
f.close()
'''
import os
from random import randint

def getRandomValue(l):
    randIndex = randint(0, len(l) - 1)
    return l[randIndex]


numFiles = 10 # nombre de fichiers à générer
fileNames = ["script", "demo", "example", "test"]
extensions = ["txt", "log", "json", "js", "exe"]
targetDir = "files/"



# for x in range(numFiles):
#     fileName = targetDir + getRandomValue(fileNames) + "." + getRandomValue(extensions)
#     # print(fileName)
#     f = open(fileName, "w")
#     f.close
#     print("Création du fichier '%s'" %fileName)

# avant de créer les fichiers, vérifier que le dossier existe
# dirExists = os.path.isdir(targetDir)
# if not dirExists:
#     print("Le dossier '%s' n'existe pas" % targetDir)
#     try:
#         os.mkdir(targetDir)
#         print("Le dossier cible '%s' n'existe pas" % targetDir)
#     except:
#         print("Impossible de créer le dossier %s" % targetDir)

for x in range(numFiles):
    fileName = targetDir + getRandomValue(fileNames) + "." + getRandomValue(extensions)
    print("\nTentative de création du fichier'%s' " % fileName)
    
    try:
        f = open(fileName, "x")
        f.close
        print("=> Succès")
    except:
        print("=> Erreur, le fichier n'a pas pu être créé.")
    print("Création du fichier '%s'" %fileName)