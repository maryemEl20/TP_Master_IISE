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
        return math.pi * (self.rayon ** 2)

class Rectangle(Forme):
    def __init__(self, lan, lar):
        self.lan = lan  # Longueur du rectangle
        self.lar = lar  # Largeur du rectangle

    def calculer_surface(self):
        return self.lan * self.lar 


def afficher_surface(formes):
    for forme in formes:
        print(f"la surface de {forme.__class__.__name__} est {forme.calculer_surface():.2f}") 
cercle = Cercle(10)  
rectangle = Rectangle(2, 3)  

# Liste des formes
formes = [cercle, rectangle]

# Affichage des surfaces calculées
afficher_surface(formes)
