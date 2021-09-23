# guessNumber = 42
# playerImput = int(input("Saisir un nombre entier : "))

# if (playerImput) == guessNumber:
#     print("Bravo, tu as deviné !")
# else:
#  if playerImput > 42:
#     print("C'est moins")
#  else:
#     print("C'est plus")



guessNumber = 42


try:
   playerImput = int(input("Saisir un nombre entier : "))
except:
   print("Saisie non valide")
   exit() # sortie immédiate du programme

if (playerImput) == guessNumber:
   print("Bravo, tu as deviné !")
else:
   if playerImput > guessNumber:
    print("C'est moins")
   else:
    print("C'est plus")

