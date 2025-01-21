import pandas as pd

# Charger le fichier CSV
fichier_csv = "./employes.csv"
df = pd.read_csv(fichier_csv)

# Afficher les cinq premières lignes du jeu de données
print("Les cinq premières lignes du fichier :")
print(df.head())

# Calculer et afficher la moyenne de l'âge des employés
moyenne_age = df['Age'].mean()
print("\nLa moyenne d'âge des employés est :", moyenne_age)

# Calculer la moyenne des salaires des employés
moyenne_salaire = df['Salaire'].mean()
print("La moyenne des salaires des employés est :", moyenne_salaire)

