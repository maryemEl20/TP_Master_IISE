#Fonctions avec des arguments par défaut
def salutation(nom, message="Bonjour"):
    
    print(f"{message}, {nom}!")

nom = input("Entrer votre nom :")
salutation(nom)   # Utilise le message par défaut : "Bonjour"
salutation(nom, "Salut")   # Spécifie un autre message "Salut"
