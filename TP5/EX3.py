# Demander à l'utilisateur d'entrer trois phrases initiales
liste = []
for index in range(1,4):
    phrase = input(f"Éntrer phrases num {index} :")
    liste.append(phrase)

# Ouvrir le fichier en mode écriture pour enregistrer les phrases initiales
with open("phrases.txt","w") as file:
    for phrase in liste:
        file.write(phrase +"\n")

reponse = input("Souhaitez-vous ajouter d'autres phrases ? (oui/non) : ").strip().lower()
if reponse  == "oui":
    with open("phrases.txt","a") as file:
        phrase = input(f"Éntrer la phrase :")
        file.write(phrase +"\n")
elif reponse =="non":
        print("Fin du programme.")
else:
    print("oui/non ?")

print("Les phrases ont été enregistrées dans 'phrases.txt'.")

with open("phrases.txt", "r") as file:
    lignes = file.readlines()
    for ligne in lignes:
        print(f"{ligne.strip()}")



