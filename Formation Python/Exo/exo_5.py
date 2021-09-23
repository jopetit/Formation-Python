'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png
Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")

import os, shutil


fileName = "flagBis"
srcDir = "flags"
dirExists = os.path.isdir(fileName)



if not dirExists:
  print("Le dossier cible '%s' n'existe pas" % fileName)
  try:
    os.mkdir(fileName)
    print("Le dossier cible '%s' a été créé" % fileName)
  except:
    print("Impossible de créer le dossier cible '%s'" % fileName)
    exit()

for f in os.listdir(srcDir):
  if not f == "missing.png":
    shutil.copyfile(
      srcDir + "/" + f,
      fileName + "/" + f[:2].upper() + ".png"
    )
  print("Drapeau '%s' copié et renommé" % f)
