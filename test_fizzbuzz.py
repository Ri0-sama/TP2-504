import unittest
from fizzbuzz import fizzBuzz

class testFizzBuzz(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = fizzBuzz("MonObjet")

        
        # Test avec des assertions correctes

    def test_affiche_n5(self):
        result = self.instance.affiche(5)
        print(f"Résultat pour n=5 : {result}")
        self.assertEqual(self.instance.affiche(5), "12Fizz4Buzz")  

    def test_affiche_n15(self):
        result = self.instance.affiche(15)
        print(f"Résultat pour n=15 : {result}")
        self.assertEqual(self.instance.affiche(15), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")  

    def test_affiche_n3(self):
        result = self.instance.affiche(3)
        print(f"Résultat pour n=3 : {result}")
        self.assertEqual(self.instance.affiche(3), "12Fizz")  


if __name__ == "__main__":
    unittest.main()
