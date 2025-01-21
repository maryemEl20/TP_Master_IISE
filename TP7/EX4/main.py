# main.py

from src.math_operations import additionner, soustraire, multiplier, diviser
from src.string_operations import concatener, to_upper

def main():
    
    while True:
        # Affichage du menu des opérations
        print("\nChoisissez une opération :")
        print("1. Opérations mathématiques")
        print("2. Opérations sur les chaînes")
        print("3. Quitter")

        choix = input("Entrez votre choix (1/2/3) : ")

        if choix == "1":
            # Opérations mathématiques
            print("\nOpérations mathématiques :")
            print("1. Addition")
            print("2. Soustraction")
            print("3. Multiplication")
            print("4. Division")
            
            operation = input("Choisissez une opération mathématique (1/2/3/4) : ")
            
            if operation in ["1", "2", "3", "4"]:
                # Demander les deux nombres
                try:
                    num1 = float(input("Entrez le premier nombre : "))
                    num2 = float(input("Entrez le deuxième nombre : "))
                    
                    if operation == "1":
                        print(f"Résultat de l'addition : {additionner(num1, num2)}")
                    elif operation == "2":
                        print(f"Résultat de la soustraction : {soustraire(num1, num2)}")
                    elif operation == "3":
                        print(f"Résultat de la multiplication : {multiplier(num1, num2)}")
                    elif operation == "4":
                        print(f"Résultat de la division : {diviser(num1, num2)}")

                except ValueError:
                    print("Erreur : Veuillez entrer des nombres valides.")
                except ZeroDivisionError:
                    print("Erreur : Division par zéro.")
            else:
                print("Opération non valide.")
        
        elif choix == "2":
            # Opérations sur les chaînes
            print("\nOpérations sur les chaînes :")
            print("1. Concaténer des chaînes")
            print("2. Mettre une chaîne en majuscules")
            
            operation = input("Choisissez une opération sur les chaînes (1/2) : ")
            
            if operation == "1":
                # Demander les deux chaînes à concaténer
                string1 = input("Entrez la première chaîne : ")
                string2 = input("Entrez la deuxième chaîne : ")
                print(f"Résultat de la concaténation : {concatener(string1, string2)}")
            
            elif operation == "2":
                # Demander la chaîne à convertir en majuscules
                string = input("Entrez la chaîne à mettre en majuscules : ")
                print(f"Résultat en majuscules : {to_upper(string)}")
            
            else:
                print("Opération non valide.")
        
        elif choix == "3":
            print("Merci d'avoir utilisé l'application !")
            break
        else:
            print("Choix non valide, veuillez réessayer.")

if __name__ == "__main__":
    main()
