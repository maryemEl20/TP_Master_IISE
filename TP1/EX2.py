def max_tuple(t):

    if not t:  # Vérifie si le tuple est vide
        return "Vide"

    max = t[0]  # Initialise le maximum au premier élément
    for nombre in t:
        if nombre > max:
            max = nombre
    return f"Le plus grand nombre dans le tuple : {max}" 
   # return max(t)   :return: Le plus grand nombre dans le tuple

t = (1,5,3)
print(max_tuple(t))  

