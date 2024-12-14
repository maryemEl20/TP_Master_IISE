
class CompteBancaire:
    
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self,montant):
        if montant > 0:
            self.solde +=montant
            print(f"{montant} déposé ")
        else :
            print("Le montant doit être positif.")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"{montant} retiré ")
        else:
            print("le solde doit être suffisant")
    
    def afficher_solde(self):
        print(f"Le solde actuel de {self.titulaire} est {self.solde}.")

compte = CompteBancaire("Ali", 500)
compte.afficher_solde()

compte.deposer(200)
compte.afficher_solde()

compte.retirer(2000)
compte.afficher_solde()

compte.retirer(100)
compte.afficher_solde()


