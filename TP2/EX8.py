# Définition de la classe Personne
class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.amis = []  # Liste pour stocker les amis

    def __str__(self):
        return f"Personne : {self.nom}, Nombre d'amis : {len(self.amis)}"
    # Méthode pour ajouter un ami

    def ajouter_ami(self, ami):
        if ami not in self.amis:  # Évite les doublons
            self.amis.append(ami)
            print(f"{ami.nom} comme ami de {self.nom}.")
        else:
            print(f"{ami.nom} est un ami de {self.nom}.")

    # Méthode pour afficher les amis
    def afficher_amis(self):
        if not self.amis:
            print(f"{self.nom} n'a pas d'amis.")
        else:
            print(f"\nLes amis de {self.nom} sont :")
            for ami in self.amis:
                print(f"- {ami.nom}")

# Création de personnes
personne1 = Personne("Ali")
personne2 = Personne("Nor")
personne3 = Personne("Hassan")
<<<<<<< HEAD

=======
>>>>>>> 8b1c6e98dba08c507fa9b9cfb2453a23d4328ca2

# Ajout d'amis
personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)
personne1.ajouter_ami(personne2)

# Affichage des amis de chaque personne
personne1.afficher_amis()
personne2.afficher_amis()

print(personne1)  # Appel de la méthode __str__
