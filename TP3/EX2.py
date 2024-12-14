class Personne:
    # Initialisation de la classe avec des attributs privés
    def __init__(self, nom, prenom, age):
        self.__nom = nom  # Attribut privé pour le nom
        self.__prenom = prenom  # Attribut privé pour le prénom
        self.__age = age  # Attribut privé pour l'âge

    # Méthode pour obtenir le nom
    @property
    def nom(self):
        return self.__nom

    # Méthode pour obtenir le prénom
    def get_prenom(self):
        return self.__prenom

    # Méthode pour obtenir l'âge
    def get_age(self): 
        return self.__age
    
    @property
    def age(self):
        return self.__age

    # Méthode pour modifier le nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    # Méthode pour modifier le prénom
    def set_prenom(self, prenom):
        self.__prenom = prenom

    # Méthode pour modifier l'âge
    def set_age(self, age):
        self.__age = age

    @age.setter
    def age(self, age):
        self.__age = age

    # Représentation sous forme de chaîne de l'objet
    def __str__(self):
        return f"Nom et Prenom: {self.__nom} {self.__prenom}, Age : {self.__age}"

personne = Personne("Ali", "Gziri", 20)  
print(personne)  # Affichage des informations de l'objet
print(personne.nom,"", personne.get_prenom())  # Affichage du nom et du prénom

# Modification de l'âge 1
personne.set_age(21)
print(personne.get_age())   #Affichage des informations après modification

## Modification de l'âge 2
personne.age = 30
print(personne.age)         #Affichage des informations après modification