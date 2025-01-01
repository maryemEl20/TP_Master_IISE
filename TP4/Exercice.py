class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque = marque
        self.modele = modele
        self.annee  = annee

    def afficher_info(self):
         print(f"La marque :{self.marque}\nModele :{self.modele}\nAnnee :{self.annee} ")

class Moteur:
    def __init__(self,puissance,type_moteur): 
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_Moteur(self):
        print(f"La puissance du moteur :{self.puissance}\nLe type de moteur :{self.type_moteur} ") 

class Voiture(Vehicule,Moteur):
    def __init__(self, marque, modele, annee,puissance,type_moteur,nombre_de_places):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_de_places = nombre_de_places
    
    def afficher_info(self):
        super().afficher_info()
        super().afficher_Moteur()
        print(f"Nombre de places :{self.nombre_de_places}")
    
class Moto(Vehicule,Moteur):
    def __init__(self, marque, modele, annee,puissance,type_moteur,type_moto):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        super().afficher_info()
        super().afficher_Moteur()
        print(f"Le type de moto :{self.type_moto}") 

voiture = Voiture("BMW", "X5", 2020, 300, "Essence", 5)
moto = Moto("Davidson", "Street 750", 2020, 47, "Essence", "Cruiser")

voiture.afficher_info()
print("-----------------------------")
moto.afficher_info()

print(Voiture.mro())