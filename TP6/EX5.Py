"""""
Écrivez une fonction `process_input(user_input)` qui tente de convertir `user_input` en entier et
d'effectuer une division par 10. Gérez les exceptions `ValueError` et `ZeroDivisionError` dans des
blocs `except` séparés, en affichant des messages d'erreur appropriés.
"""""
def process_input(user_input):
    try:
        # Try to convert user_input to an integer
        value = int(user_input)
        # Try to divide by 10
        result = 10 / value
        return result
    except ValueError:
        return f"Error: '{user_input}' is not a valid integer"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    
while True:
    user_input = input("Entrez un number : ")
    print(process_input(user_input))
   

   