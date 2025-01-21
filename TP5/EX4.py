import csv

contacts =  [ ["Nom","Age","Ville"],
            ["Maryem","22","Agadir"],
            ["Sara","24","Tanger"],
            ["Ali","24","Tanger"],
            ]


# Écrire les données des contacts
with open("contacts.csv",mode='w',newline='') as csvfile:
    write = csv.writer(csvfile)  
    write.writerows(contacts)  


# Lecture du fichier "contacts.csv"
with open("contacts.csv",mode='r',newline='') as csvfile:
    reader = csv.reader(csvfile)  
    for i,row in enumerate(reader):
        if i ==0:
            continue
        print(f"Nom : {row[0]} , Age :{row[1]} , Ville : {row[2]}")