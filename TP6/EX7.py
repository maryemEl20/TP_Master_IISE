"""""
Utilisez le module `logging` pour créer une fonction `log_error(message)` qui enregistre les erreurs
dans un fichier `error.log`. Modifiez l'exercice 3 pour utiliser cette fonction pour enregistrer une
erreur si le fichier n'est pas trouvé.
"""""

import logging
logging.basicConfig(filename='error.log', format= '%(message)s')

def log_error(message):
    logging.error(message)

def read_file(file_name):
    try:
        file = open(file_name, "r")
        content = file.readlines()
        for ligne in content:
            print(f"{ligne.strip()}")
    except FileNotFoundError:
        error_message = f"Error: The file '{file_name}' does not exist."
        print(error_message)
        log_error(error_message)  # Enregistrer l'erreur dans error.log
    finally:
        print("Fin du traitement\n")   

file_name = "ex.txt" 
read_file("non_existent_file.txt") 
read_file(file_name) 

file_name = "exemple.txt" 
read_file(file_name) 

