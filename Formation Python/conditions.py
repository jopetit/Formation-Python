isEarthRound = True
message = "2 est strictement supérieur à 1"
condition = 2 > 1 #équivalent condition = True

if isEarthRound == True:
    print("La Terre est ronde")

# Version courte
if isEarthRound :
    print('La Terre est ronde')

if condition :
    print(message)

n = 5
observeFiFaRules = False


if n >= 7 and observeFiFaRules:
    print("Assez pour jouer au foot")
else:
    print("Le nombre de joueurs est insuffisant pour jouer au foot")

exemple1 = False or True
exemple2 = False and True
exemple3 = not False
print("False or True =>", exemple1)
print("False and True =>", exemple2)
print("not False =>", exemple3)
