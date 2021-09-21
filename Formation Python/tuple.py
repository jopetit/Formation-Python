t = () # tuple vide
print (type(t)) # <class 'tuple'>

# lat = 45.9632
# lng = 21.7891

coordGps = (45.9632, 21.7891)
print("Latitude:", coordGps[0])
# print("Longitude:", coordGps[2]) # IndexError: tuple index out of range
print("Longitude:", coordGps[1])

lat, lng = coordGps
print("Latitude:", lat, "Longitude:", lng)

# coordGps[0] = 66.3344 #TypeError: 'tuple' object does not support item assignment => les tuples ne s'accèdent qu'en lecture seule
coordGps[2] = 66.3344

