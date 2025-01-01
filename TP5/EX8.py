
try:
    with open("inexistant.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: The file 'inexistant.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
