
def safe_division(a, b):
    try:
        result = a/b
        print("Result :", result)
    except ZeroDivisionError:
        print("Error : Division by zero is not allowed.")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return f"Failed to convert '{value}' to an integer."
      

def read_file(file_name):
    try:
        # Open and read the file
        file = open(file_name, "r")
        content = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    else : 
        for ligne in content:
            print(f"{ligne.strip()}")
    finally:
        print("\nFin du traitement")   

