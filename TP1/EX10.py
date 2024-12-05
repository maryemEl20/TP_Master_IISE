def fusionner_dicts(dict1, dict2):
    dict  = dict1
    
    for k,valeur in dict2.items():
        # Si la clé est déjà présente, additionner les valeurs
        if k in dict:
            dict[k] += valeur
        else:
            # Sinon, ajouter la nouvelle clé avec sa valeur
            dict[k] = valeur
    
    return dict

dict1 = {'pomme': 10, 'banana': 20, 'kiwi': 30}
dict2 = {'kiwi': 10, 'banana': 20, 'orange': 50}

print(fusionner_dicts(dict1, dict2)) #{'pomme': 10, 'banana': 40, 'kiwi': 40, 'orange': 50}
