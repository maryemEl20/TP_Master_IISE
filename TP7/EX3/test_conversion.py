import unittest
import sys
import os

# Ajouter le dossier parent (contenant EX1) au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importer les fonctions depuis EX1.conversion
from EX1.conversion import dollars_to_dirhams,meters_to_kilometers

class TestModule(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        with self.assertRaises(ValueError):
            dollars_to_dirhams(-10)  # Montant négatif
     
    def test_meters_to_kilometers(self):
        with self.assertRaises(ValueError):
            meters_to_kilometers(-1000) # Distance négative
   
if __name__ == '__main__':
    unittest.main()
