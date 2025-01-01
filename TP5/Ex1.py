# Création du fichier texte "exemple.txt"

# Ouvrir le fichier en mode lecture
with open("exemple.txt", "r") as fichier:
    lignes = fichier.readlines()
    
    # Afficher chaque ligne avec son numéro
    for index,ligne in enumerate(lignes,start=1):
        print(f"{index}: {ligne.strip()}")
