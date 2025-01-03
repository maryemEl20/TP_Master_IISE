"""""
Écrivez un programme qui demande à l'utilisateur de saisir un fichier, puis un entier. Utilisez les
concepts de gestion des exceptions pour garantir que le fichier est lu avec succès et que l'entier est
valide.
Gérer toutes les exceptions appropriées et afficher des messages utiles.
"""""

def read_file(file_name):
    try:
        file = open(file_name, "r")
        content = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Erreur : Le fichier '{file_name}' n'a pas été trouvé.")
    except IOError:
        raise IOError(f"Erreur : Impossible de lire le fichier '{filename}'.")
    else : 
        print("Contenu du fichier : ")
        for ligne in content:
            print(f"{ligne.strip()}")
    finally:
        print("\nFin du traitement")   


def get_positive_integer():
    while True:
        try:
            user_input = int(input("Veuillez entrer un entier positif: "))
            if user_input <= 0:
                print("L'entier doit être positif. Essayez encore.")
            else:
                print(f"L'entier est : {user_input}")
                return user_input # Sortir de la boucle lorsque la saisie est valide
        except ValueError:
            print("Ce n'est pas un entier valide. Veuillez entrer un entier.")


# Exécution du programme
try:
    filename = input("Veuillez entrer le nom du fichier à lire : ")
    read_file(filename)  

    # Demande à l'utilisateur un entier valide
    get_positive_integer()
        
except FileNotFoundError as efile:
    print(efile)  
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")