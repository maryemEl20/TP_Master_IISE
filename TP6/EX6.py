"""""
Modifiez l'exercice 1 pour inclure un bloc `else` qui imprime un message indiquant que la division
a été effectuée avec succès, et un bloc `finally` qui indique que la fonction est terminée, quel que
soit le résultat.
"""

def safe_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print(e)
    else:
        print(f"Result: {result}")
    finally:
        print("Function execution completed.")


safe_division(10,0) #Division by zero

safe_division(10,5) #Result : 2.0