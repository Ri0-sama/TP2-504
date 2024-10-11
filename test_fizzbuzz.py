import unittest
from fizzbuzz import fizzBuzz

class testFizzBuzz (unittest.TestCase):

    def setUp(self) -> None:
        self.instance = fizzBuzz("MonObjet")


    def test_fizzBuzz(self):
        self.assertEqual(self.instance.affiche(), "dgjbnldhssglhlh")


if __name__=="__main__":
    unittest.main()