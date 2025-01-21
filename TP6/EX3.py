"""""
Écrivez une fonction `read_file(filename)` qui tente d'ouvrir et de lire un fichier. Si le fichier
n'existe pas, la fonction doit gérer l'exception `FileNotFoundError` et imprimer un message d'erreur.
Utilisez également un bloc `finally` pour garantir que le fichier est fermé.
"""""
def read_file(file_name):
    try:
        # Open and read the file
        file = open(file_name, "r")
        content = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    else : 
        for ligne in content:
            print(f"{ligne.strip()}")
    finally:
        if 'file' in locals():
            file.close()
    print("\nFin du traitement")   

file_name = "exemple.txt" 
read_file(file_name) 
read_file("non_existent_file.txt") 




