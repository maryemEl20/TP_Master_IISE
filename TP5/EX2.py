# Demander à l'utilisateur d'entrer trois phrases initiales
liste = []
for index in range(1,4):
    phrase = input(f"Entrer phrases num {index} :")
    liste.append(phrase)

# Ouvrir le fichier en mode écriture pour enregistrer les phrases initiales
with open("phrases.txt","w") as file:
    for phrase in liste:
        file.write(phrase +"\n")

print("Les phrases ont été enregistrées dans 'phrases.txt'.")
