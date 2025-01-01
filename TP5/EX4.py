import csv

contacts =  [ ["Nom","Age","Ville"],
            ["Maryem","22","Agadir"],
            ["Sara","24","Tanger"],
]

# Écrire les données des contacts
with open("contacts.csv",mode='w',newline='') as csvfile:
    write = csv.writer(csvfile)  
    write.writerows(contacts)  


# Lecture du fichier "contacts.csv"
with open("contacts.csv",mode='r',newline='') as csvfile:
    reader = csv.reader(csvfile)  
    for row in reader:
        print(row)