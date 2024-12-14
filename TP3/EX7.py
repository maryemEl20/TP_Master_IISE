from abc import ABC,abstractmethod
class Vehicule(ABC):
    @abstractmethod
    def deplacer(self,lieu):
        pass
class Voiture(Vehicule):
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
    
    def deplacer(self,lieu):
        print(f"{self.marque} de {self.modele} se deplace sur {lieu}")

class Bicyclette(Vehicule):
    def __init__(self, marque, type):
        self.marque = marque
        self.type = type

    def deplacer(self,lieu):
        print(f"{self.marque} de {self.type} se deplace sur {lieu}")

voiture = Voiture("BMW", "Model 01")
bicyclette = Bicyclette("Giant","Type 02")

voiture.deplacer("la route")
bicyclette.deplacer("le sentier")    



        
        