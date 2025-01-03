"""""
Écrivez des tests unitaires pour vérifier que les exceptions sont levées correctement dans les
fonctions que vous avez créées dans les exercices précédents. Utilisez le module `unittest` pour
cela.
"""""
import unittest
from my_module import safe_division,convert_to_int,read_file

class TestModule(unittest.TestCase):

    def test_safe_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)
        self.assertEqual(safe_division(10, 2), 5.0)

    def test_convert_to_int(self):
        with self.assertRaises(ValueError):
            convert_to_int('abc')
        self.assertEqual(convert_to_int('10'), 10)

    def test_read_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file('non_existent_file.txt')
   
# Exécution des tests
if __name__ == '__main__':
    unittest.main()
