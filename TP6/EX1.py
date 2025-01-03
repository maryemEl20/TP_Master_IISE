
"""""
Écrivez une fonction `safe_division(a, b)` qui prend deux arguments et renvoie le résultat de la
division de `a` par `b`. Si `b` est zéro, la fonction doit lever une exception 
`ZeroDivisionError` avec un message approprié.
"""""
def safe_division(a, b):
    try:
        result = a/b
        print("Result :", result)
    except ZeroDivisionError:
        print("Error : Division by zero is not allowed.")

#Error : Division by zero is not allowed.
safe_division(10,0)
#Result : 2.0
safe_division(10,5)