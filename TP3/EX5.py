class Employe:
    def __init__(self,nom,prenom,salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_info(self):
        print(f"Nom: {self.nom}, Prenom: {self.prenom}, Salaire: {self.salaire} DH")

class Manager(Employe):
    def __init__(self,nom,prenom,salaire):
        super().__init__(nom,prenom,salaire)
        self.employes_supervises = []

    def ajouter_employes(self,employe):
        self.employes_supervises.append(employe)

    def afficher_employes(self):
        for employe  in self.employes_supervises:
            employe.afficher_info()
         

employe1 = Employe("Ali","ELBAZ",5000)
employe2 = Employe("Sara","MOJAD",5500)

manage =Manager("Saad","ALANI",5900)
manage.ajouter_employes(employe1)
manage.ajouter_employes(employe2)

manage.afficher_info()
manage.afficher_employes()