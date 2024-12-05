#Analyser un texte

def analyse_texte(texte):
    D = {"mots" : 1,"caracteres" :0}

    if not texte:
        return "Vide"
    
    for i in texte :
        if i == " ":
            D["mots"] +=1
        else :
            D["caracteres"]+=1

    return D

# Exemple d'utilisation
texte = "Bonjour Ali"
resultat = analyse_texte(texte)
print(resultat)
