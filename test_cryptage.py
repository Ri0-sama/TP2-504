import unittest
from cryptage import Cryptage

class TestCryptage(unittest.TestCase):
    def setUp(self):
        self.instance = Cryptage()

    

    def test_crypt_message_with_shift(self):
        self.assertEqual(self.instance.crypt("abc", 2), "cde")  # Test échouera ici

if __name__ == "__main__":
    unittest.main()
