# Définition de la classe Livre

class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

# la méthode __str__ transforme l'objet en une représentation lisible
# l'affichage beaucoup plus informatif et convivial
      
    def __str__(self):
        return f"'{self.titre}' de {self.auteur} ({self.annee_publication})"

# Définition de la classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.liste_livres = []

    def ajouter_livre(self, livre):
        self.liste_livres.append(livre)
        print(f"Livre ajouté: {livre}")

    def afficher_livres(self):
        if not self.liste_livres:
            print("Vide.")
        else:
            print("\nLivres dans la bibliotheque :\n")
            for livre in self.liste_livres:
                print(f"* {livre}")

# Créer une bibliothèque

bibliotheque = Bibliotheque()

# Créer des livres
livre1 = Livre("L'Enfant de sable", "Tahar Ben Jelloun", 1985)
livre2 = Livre("Les Voix de Marrakech", "Elias Canetti", 1967)
livre3 = Livre("Le Pain nu", "Mohamed Choukri", 1972)  

# Ajouter les livres à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Afficher tous les livres de la bibliothèque
bibliotheque.afficher_livres()
