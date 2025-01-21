
def dollars_to_dirhams(dollars):
    if dollars < 0:
        print("Le montant en dollars ne peut pas être négatif.")
    else:
        taux_conversion = 10.5  # Taux de conversion (1 USD = 10.5 MAD)
        result =  dollars * taux_conversion 
        print(f"{dollars} dollars = {result} dirhams.")


def meters_to_kilometers(meters):
    if meters < 0:
        print("La distance en mètres ne peut pas être négative.")
    else:
        taux_conversion = 0.001  # Taux de conversion (1 m = 0.001 km)
        result = meters * taux_conversion
        print(f"{meters} metres = {result} kilometres.")

   





