#POO : Programmation Orienté Objets

class Student:
    # attributs/propriétés
    firstname = "xxx"
    lastname = "yyy"
    email ="test@test.fr"
    member = True

# méthodes (fonction définie à l'intérieur d'une classe)

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getFullName(self):
        return self.firstname + " " + self.lastname

    def getInitials(self):
        return (self.firstname[:1] + self.lastname[:1]).upper()
    
    def remove(self):
        return self.member

# méthode d'accès en écriture sur les propriétés ciblés(setters)
    def setFirstName(self, firstname):
        self.firstname = firstname

    def setLastName(self, lastname):
        self.lastname = lastname

student1 = Student() # instancie la classe Student => à partir d'une class, on produit une instance
student2 = Student()
student3 = Student()

student1.setFirstName("Roberto")
student1.setLastName("BAGGIO")

student2.setFirstName("Alessandro")
student2.setLastName("NESTA")

student1.remove()

# print(student1.firstname)
print(student1.getFirstName())
print(student1.getLastName())
print(student1.getFullName())
print(student1.getInitials())

if student2.member:
    print(student2.getFullName(), "est membre de l'établissement")

if student1.member:
    print(student1.getFullName(), "est membre de l'établissement")
else:
    print(student1.getFullName(), "n'est plus membre de l'établissement")