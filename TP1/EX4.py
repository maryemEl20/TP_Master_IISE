def compte_occurences(liste):
 
    dic = {}
    for mot in liste:
        if mot not in dic:
            dic[mot] = 1
        else:
            dic[mot] += 1
    return dic #Dictionnaire où les clés sont les mots et les valeurs sont leurs occurrences

liste = ["orange", "banana", "orange","kiwi","orange"]
mots = compte_occurences(liste)
print(mots)
