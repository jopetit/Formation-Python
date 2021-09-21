'''
*** Exo 3 ***
Ecrire un script python qui calculera et affichera pour chacun des prix le
prix TTC.
Créer une fonction qui calculera le prix TTC du prix HT qu'on lui fournira
en entrée.

'''

# prices = [10,100,30,10,8] # prix HT
# vat = 20 # 20%

# def ttc(ht):
#     return ht * (1+(vat/100))

# for p in prices:
#     print(ttc(p))

# correction

prices = [14,100,30,10,8] # prix HT
vat = 20 # 20%

def getPriceWithVat(price, vat = 20):
    return round(price *(1 + vat/100), 2)

#print(getPriceWithVat(100))

for price in prices:
    print(getPriceWithVat(price, 7))
