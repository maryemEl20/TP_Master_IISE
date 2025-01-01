import os
import shutil

# Step 1: Create the file "journal.txt"
with open("journal.txt", "w", encoding="utf-8") as file:
    file.writelines([
        "Today, I learned how to manipulate files using Python.\n",
        "It's a powerful and versatile programming language.\n",
        "I will keep practicing to improve my skills.\n"
    ])
print("The file 'journal.txt' has been successfully created.")

# Step 2: Copy the file
shutil.copy("journal.txt", "journal_copie.txt")
print("The file 'journal.txt' has been copied as 'journal_copie.txt'.")

# Step 3: Create the folder and move the copied file
source = "journal_copie.txt"
dossier = "archives/journal_copie.txt"

shutil.move(source,dossier)
print("The file 'journal_copie.txt' has been moved to the 'archives' folder.")
