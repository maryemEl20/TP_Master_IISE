def intersection(ensemble1, ensemble2):

    s = set()
    for e in ensemble1:
        if e in ensemble2:
            s.add(e)
    return s   #return: Nouvel ensemble contenant les éléments communs aux deux ensembles

ensemble1 = {1, 2, 3, 4}
ensemble2 = {2, 4, 3, 6}

resultat = intersection(ensemble1, ensemble2)
print("Intersection :", resultat)  #Intersection : {2, 3, 4}
