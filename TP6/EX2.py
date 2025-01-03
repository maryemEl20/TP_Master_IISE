"""""
Créez une fonction `convert_to_int(value)` qui tente de convertir `value` en entier. Si `value` n'est
pas convertible, la fonction doit lever une exception `ValueError` avec un message indiquant que la
conversion a échoué.
"""""
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return f"Failed to convert '{value}' to an integer."

print("Converted value:", convert_to_int("123"))
print("Converted value:", convert_to_int("abcd"))

