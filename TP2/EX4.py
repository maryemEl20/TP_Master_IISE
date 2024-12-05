
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Salut !, je suis {self.prenom} {self.nom} et j'ai {self.age} ans.")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"{self.prenom} {self.nom} de matricule {self.matricule} est etudie.")

personne = Personne("Ali", "Gziri", 30)
personne.se_presenter()

etudiant = Etudiant("Ali", "Gzal", 22, "ID23")
etudiant.se_presenter()  
etudiant.etudier()  
