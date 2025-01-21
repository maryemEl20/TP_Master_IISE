"""""
Créez une exception personnalisée `NegativeAgeError`. Écrivez une fonction `set_age(age)` qui
lève cette exception si l'âge est négatif. Testez la fonction dans un bloc `try` et gérez l'exception en
imprimant un message approprié.
"""""
class NegativeAgeError(Exception):
    pass
def set_age(age):
    if age < 0:
        raise NegativeAgeError(f"Invalid age: {age}. Age cannot be negative.")
    print(f"Age set to: {age}")
    
try:
    set_age(22)  
    set_age(-1)  
except NegativeAgeError as e:
    print("Error:", e) #Affiche "Error: Invalid age: -1. Age cannot be negative."