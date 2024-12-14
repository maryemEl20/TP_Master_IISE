# Classe Produit
class Produit:
    def __init__(self,nom,prix):
        self.__nom = nom
        self.__prix = prix
    @property
    def nom(self):
        return  self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
        
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,prix):
        if prix > 0 :
             self.__prix = prix
        else:
           raise ValueError("Le prix doit être positif.")

    
# Classe Commande
class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.prix * self.quantite

    def afficher_commande(self):
        self.produit
        print(f"Quantites: {self.quantite}, Total : {self.calculer_total()}")

# Classe Panier
class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total_panier(self):
        total = 0
        for commande in self.commandes:
            total += commande.calculer_total()
        return total

    def afficher_panier(self):
        for commande in self.commandes:
            commande.afficher_commande()
        print(f"Total du panier: {self.calculer_total_panier()}")

# Exemple d'utilisation
produit1 = Produit("shirt", 25)
produit2 = Produit("Pantalon", 40)
produit3 = Produit("Chausstum", 60)

commande1 = Commande(produit1, 2)  
commande2 = Commande(produit2, 3) 
commande3 = Commande(produit3, 1) 

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)
panier.ajouter_commande(commande3)

panier.afficher_panier()
