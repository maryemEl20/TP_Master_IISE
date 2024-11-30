#Fonctions variadiques

def somme_varargs(*args):
    S = 0
    for i in args:
        S+= i
    return S # retourne la somme de ces arguments

ma_liste = [1, 2, 3, 4]
print("La somme est :",somme_varargs(*ma_liste))
print("La somme est :",somme_varargs(1,2,3,4,5))