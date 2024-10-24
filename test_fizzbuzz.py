import unittest
from fizzbuzz import fizzBuzz

class testFizzBuzz(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = fizzBuzz("MonObjet")


# Tests avec des assertions incorrectes
    def test_affiche_n5(self):
        
        self.assertEqual(self.instance.affiche(5), "12Fizz4BuzzA")  # 'A' est incorrect

    def test_affiche_n15(self):
        self.assertEqual(self.instance.affiche(15), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBeeB")  # 'B' est incorrect

    def test_affiche_n3(self):
        self.assertEqual(self.instance.affiche(3), "12FizzC")  # 'C' est incorrect

if __name__ == "__main__":
    unittest.main()
