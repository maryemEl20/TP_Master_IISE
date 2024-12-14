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
        
    def calculer_prix_avec_remise(self,remise,montant):
        if self.__prix > montant:
            return self.__prix * (1 - remise /100)
        return self.__prix

produit = Produit("Laptop",3000)
print(f"prix initial {produit.prix} dh")
prix_remise = produit.calculer_prix_avec_remise(10,1500)
print(f"prix avec remise {prix_remise} dh")


        
    