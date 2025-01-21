from conversion import dollars_to_dirhams,meters_to_kilometers

# Test de dollars_to_dirhams
try:
    dollars = float(input("Entrez un montant en dollars : "))
    dollars_to_dirhams(dollars)
except ValueError as e:
    print(f"Erreur : {e}")

# Test de meters_to_kilometers
try:
    meters = float(input("\nEntrez une distance en mètres : "))
    meters_to_kilometers(meters)
except ValueError as e:
    print(f"Erreur : {e}")
