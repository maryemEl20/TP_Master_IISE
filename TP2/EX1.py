class Chien :
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age
        
    def aboyer(self):
        print("Woof!")

chien = Chien("LOOK", "Lab", 110)
chien.aboyer()
print(f"Nom : {chien.nom} ,Race : {chien.race } ,Age : {chien.age}")
