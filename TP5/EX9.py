file_name = "journal.txt"  

try:
    # Open and read the file
    with open(file_name, "r") as file:
        content = file.readlines()

    # Calculate statistics
    total_lines = len(content)
    total_words = sum(len(line.split()) for line in content)
    total_characters = sum(len(line) for line in content)

    # Display the results
    print(f"File statistics for '{file_name}':")
    print(f"- Total lines: {total_lines}")
    print(f"- Total words: {total_words}")
    print(f"- Total characters: {total_characters}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
