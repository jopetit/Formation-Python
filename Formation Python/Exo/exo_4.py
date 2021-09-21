'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Exemples de valeurs saisies par l'utilisateur:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''
print("*** EXO 4: somme de saisies ***")

inputNumber = int(input("Merci de saisir un chiffre : "))
guessNumber = 0
totalEntries = 0


while inputNumber != guessNumber:
  if inputNumber > guessNumber:
    print("Ce n'est pas le chiffre recherché")
    totalEntries = totalEntries + inputNumber
    
  else:
    print("Le chiffre recherché n'est pas négatif")
    totalEntries = totalEntries + inputNumber
    
  inputNumber = int(input("Devine le chiffre mystère: "))

print("Bravo ! Le chiffre recherché était bien \"0\"!", "=> la somme des valeurs saisies est :", totalEntries)
