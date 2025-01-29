
import os

def safe_division(a, b):
    try:
        result = a/b
        return f"Result :", result
    except ZeroDivisionError:
        print(f"Error : Division by zero is not allowed.")
        raise ZeroDivisionError() 


def convert_to_int(value):
    if isinstance(value, int):
        print(value) 
    elif isinstance(value, str) and (value.lstrip('-').isdigit()):
        print(int(value))
    else:
        print(f"Failed to convert '{value}' to an integer.") 
      
def read_file(file_name):
  
    if os.path.exists(file_name):
        # File exists, read its content
        file = open(file_name, "r")
        content = file.readlines()
        file.close()  # Close the file after reading
        for ligne in content:
            print(f"{ligne.strip()}")
    else:
        # File does not exist
        print(f"Error: The file '{file_name}' does not exist.")

