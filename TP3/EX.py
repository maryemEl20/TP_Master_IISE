from abc import ABC, abstractmethod
import math


class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass  

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon  # Rayon du cercle

    def calculer_surface(self):
        # Calcul de la surface d'un cercle 
        return math.pi * (self.rayon ** 2)

class Rectangle(Forme):
    def __init__(self, lon, lar):
        self.lon = lon  # Longueur du rectangle
        self.lar = lar  # Largeur du rectangle

    def calculer_surface(self):
        # Calcul de la surface d'un rectangle : longueur * largeur
        return self.lon * self.lar 

# Exemple d'utilisation
if __name__ == "__main__":
    cercle = Cercle(10)  
    rectangle = Rectangle(2, 3)  

    # Affichage des surfaces calculées
    print(f"Surface du cercle : {cercle.calculer_surface():.2f}")
    print(f"Surface du rectangle : {rectangle.calculer_surface():.2f}")
