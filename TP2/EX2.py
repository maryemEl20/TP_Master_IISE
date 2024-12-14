class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def afficher_info(self):
        print(f"Marque : {self.marque}, Modele : {self.modele}, Annee : {self.annee}")
    
Voiture1 = Voiture("Toyota", "Model 1", 2020)
voiture2 = Voiture("Dacia", "Model 2", 2022)
voiture3 = Voiture("BMW", "Model 3", 2020)   

Voiture1.afficher_info()
voiture2.afficher_info()
voiture3.afficher_info()
