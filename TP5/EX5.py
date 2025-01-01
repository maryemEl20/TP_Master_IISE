import json

# Création du dictionnaire contenant les informations des étudiants
donnees = [
    {"Nom" : "Maryem","Age": 22,"Note":18},
    {"Nom" : "Ali","Age": 20,"Note":19},
    {"Nom" : "Saad","Age": 25,"Note":15},
]

# Enregistrement du dictionnaire dans un fichier JSON
with open("etudiants.json","w") as jsonfile:
    json.dump(donnees,jsonfile,indent=4)

# Lecture du fichier JSON
with open("etudiants.json","r") as jsonfile:
    etudiants  = json.load(jsonfile)
    # Affichage des informations de chaque étudiant
    for etudiant in etudiants :
         print(f"Nom : {etudiant['Nom']}, Age : {etudiant['Age']}, Note : {etudiant['Note']}")

