#une fonction récursive `factorielle(n)`
def factorielle(n):
   
    if n == 0 :
        return 1
    else:  
        return n * factorielle(n - 1) # retourne la factorielle d'un nombre entier `n`


print(factorielle(0))  # Sortie : 1

print(factorielle(5))  # Sortie : 120
