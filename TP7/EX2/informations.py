import os
import datetime
import math

#  Afficher le répertoire courant
current_directory = os.getcwd()
print(f"Le répertoire courant  : {current_directory}")

# Afficher la date et l'heure actuelles
current_datetime = datetime.datetime.now()
print(f"La date et l'heure actuelles : {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

# Calculer la racine carrée d'un nombre donné par l'utilisateur
number  = float(input("Entrez un nombre pour calculer sa racine carrée : "))
if number < 0:
    raise ValueError("Le nombre doit être positif ou nul.")
square_root = math.sqrt(number)
print(f"La racine carrée de {number} est : {square_root}")

