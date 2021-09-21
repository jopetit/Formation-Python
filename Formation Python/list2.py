title = "Les Trois Mousquetaires"

# for c in title:
    # print(letter))

#print(title[0])
# title[0] = 'D' TypeError: les chaînes de caractères ne sont pas accessibles en écriture

#for letter in title[0:11]:
 #   print(letter)

#print(--------------------------------------------------------)

word = ""
for letter in title[4:9]:
    word += letter

print(word)

numOccurences = 0
searchedLetter = input("Lettre à rechercher : ")

for letter in title:
    if letter == searchedLetter:
        numOccurences += 1

print("La lettre \"%s\" a été trouvée %s fois dans le titre %s" % (searchedLetter, numOccurences, title))

