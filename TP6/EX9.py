"""""
Créez une fonction `get_positive_integer()` qui demande à l'utilisateur de saisir un entier positif.
Utilisez une boucle pour continuer à demander jusqu'à ce qu'une saisie valide soit fournie. Gérez les
exceptions de conversion et vérifiez que l'entier est positif.
"""""
def get_positive_integer():
    while True:
        try:
            user_input = int(input("Veuillez entrer un entier positif: "))
            
                 # Vérifier si l'entier est positif
            if user_input <= 0:
                print("L'entier doit être positif. Essayez encore.")
            else:
                print(f"L'entier valide que vous avez saisi est : {user_input}")
                return user_input
        except ValueError:
                 # Gérer les erreurs de conversion si l'entrée n'est pas un entier
            print("Erreur : Vous devez entrer un nombre entier. Essayez encore.")

if __name__ == "__main__":
    get_positive_integer()

