import unittest

import sys
import os

# Ajouter le dossier parent (contenant "src") au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from math_operations import additionner,soustraire,multiplier,diviser

class TestMathOperations(unittest.TestCase):

    def test_additionner(self):
        self.assertEqual(additionner(3, 2), 5)

    def test_soustraire(self):
        self.assertEqual(soustraire(3, 2), 1)

    def test_multiplier(self):
        self.assertEqual(multiplier(3, 2), 6)

    def test_divide(self):
        self.assertEqual(diviser(6, 2), 3)
        # Tester la division par zéro
        with self.assertRaises(ValueError):
            diviser(6, 0)

if __name__ == "__main__":
    unittest.main()