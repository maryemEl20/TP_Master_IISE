import json

# Création du dictionnaire contenant les informations des étudiants
donnees = [
    {"Nom" : "Maryem","Age": 22,"Note":18},
    {"Nom" : "Ali","Age": 20,"Note":19},
    {"Nom" : "Saad","Age": 25,"Note":15},
]

# Enregistrement du dictionnaire dans un fichier JSON
with open("etudiants.json","w") as jsonfile:
    json.dump(donnees,jsonfile,indent=4) #utilisée pour écrire un objet Python , 4 espaces,

# Lecture du fichier JSON
with open("etudiants.json","r") as jsonfile:
    etudiants  = json.load(jsonfile) #EXTRACTION : pour lire et extraire des données JSON d'un fichier et les convertir en un objet Python
    # Affichage des informations de chaque étudiant
    for etudiant in etudiants :
         print(f"Nom : {etudiant['Nom']}, Age : {etudiant['Age']}, Note : {etudiant['Note']}")

