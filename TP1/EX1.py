def somme_liste(liste):

    S = 0
    for i in liste:
        S += i
    return S # return: Somme des nombres dans la liste

ma_liste = [1, 2, 3, 4]
print("Somme est:", somme_liste(ma_liste))
