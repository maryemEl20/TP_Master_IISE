class Animals :
    def faire_du_bruit(self):
         print("Cet animal fait du bruit.")

# Définition de la sous-classe Chien      

class Chien(Animals):
    def faire_du_bruit(self):
        print("Chien : WOOF!")

# Définition de la sous-classe Chat
class Chat(Animals):
    def faire_du_bruit(self):
        print("Chat : MEAOU!")

# Créer des instances des sous-classes

chien = Chien()
chat = Chat()


chien.faire_du_bruit()  
chat.faire_du_bruit()  



