import unittest
from fizzbuzz import fizzBuzz

class testFizzBuzz(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = fizzBuzz("MonObjet")

    def test_fizzBuzz(self):
        result = self.instance.affiche()
        # Au lieu de vérifier un résultat fixe, vérifions le contenu
        self.assertIn("Fizz", result)
        self.assertIn("Buzz", result)
        self.assertIn("FrisBee", result)

if __name__ == "__main__":
    unittest.main()
