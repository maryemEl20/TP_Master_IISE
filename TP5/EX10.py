import csv

def ajouter_contact():
    nom   = input("Nom : ")
    Age   = input("Age : ")
    Ville = input("Ville : ")
    try:
        with open("contacts.csv", "a") as fichier:
            writer = csv.writer(fichier)
            writer.writerow([nom, Age, Ville])
        print("Contact ajouté.")
    except Exception as e:
        print(f"Erreur lors de l'ajout du contact : {e}")

def afficher_contacts():
    try:
        with open("contacts.csv", "r") as fichier:
            reader = csv.reader(fichier)
            contacts = list(reader)  # Lecture de toutes les lignes
            if not contacts:
                print("Aucun contact enregistré.")
            else:
                print("Contacts:")
                for row in contacts:
                    print(", ".join(row)) # Affiche chaque contact sur une ligne
    except FileNotFoundError:
        print("Aucun contact enregistré. Le fichier n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de l'affichage des contacts : {e}")

def rechercher_contact():
    nom_recherche = input("Nom à rechercher : ")
    try:
        with open("contacts.csv", "r") as fichier:
            reader = csv.reader(fichier)
            trouve = False
            for row in reader:
                if row and row[0].lower() == nom_recherche.lower(): # Gestion des majuscules/minuscules et des lignes vides
                    print("Contact trouvé :", ", ".join(row))
                    trouve = True
            if not trouve:
                print("Contact non trouvé.")
    except FileNotFoundError:
        print("Aucun contact enregistré. Le fichier n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la recherche du contact : {e}")

def supprimer_contact():
    nom_suppression = input("Nom du contact à supprimer : ")
    try:
        with open("contacts.csv", "r") as fichier_lecture:
            reader = csv.reader(fichier_lecture)
            contacts_restants = []
            supprime = False
            for row in reader:
                if row and row[0].lower() != nom_suppression.lower():
                    contacts_restants.append(row)
                elif row and row[0].lower() == nom_suppression.lower():
                  supprime = True
        with open("contacts.csv", "w") as fichier_ecriture:
            writer = csv.writer(fichier_ecriture)
            writer.writerows(contacts_restants)
        if supprime:
            print("Contact supprimé.")
        else:
            print("Contact non trouvé.")
    except FileNotFoundError:
        print("Aucun contact enregistré. Le fichier n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la suppression du contact : {e}")

def afficher_menu():
    print("\nMenu :")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    print("5. Quitter")
    while True:
        try:
            choix = int(input("Entrez votre choix : "))
            if choix == 1:
                ajouter_contact()
            elif choix == 2:
                afficher_contacts()
            elif choix == 3:
                rechercher_contact()
            elif choix == 4:
                supprimer_contact()
            elif choix == 5:
                break  # Quitter la boucle
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

# Run the application
if __name__ == "__main__":
    afficher_menu()



