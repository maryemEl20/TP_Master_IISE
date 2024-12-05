#Créez une classe "Rectangle" avec les attributs "largeur" et "hauteur"

class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        surface =  self.largeur * self.hauteur
        print(f"Surface du rectangle : {surface}")

    def calculer_perimetre(self):
        perimetre = 2 * (self.largeur + self.hauteur)
        print(f"Perimetre du rectangle : {perimetre}")

# Créer des instances des sous-classes

rectangle = Rectangle(5, 3)

surface = rectangle.calculer_surface()
perimetre = rectangle.calculer_perimetre()