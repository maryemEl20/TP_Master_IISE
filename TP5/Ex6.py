import os

# Renommer le fichier "phrases.txt" en "anciennes_phrases.txt"
ancien_nom = "phrases.txt"
nouveau_nom = "anciennes_phrases.txt"

try:
    # Renommer le fichier
    os.rename(ancien_nom, nouveau_nom)
    print(f"The file has been renamed to '{nouveau_nom}'.")
    # Supprimer le fichier renommé
    os.remove(nouveau_nom)
    print(f"The file '{nouveau_nom}' has been deleted.")
except FileNotFoundError:
    print(f"The file '{ancien_nom}' does not exist.")
except PermissionError:
    print("Permission error. Please ensure the file is not open.")
except Exception as e:
    print(f"An error occurred: {e}")
