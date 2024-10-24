import unittest
from cryptage import Cryptage

class TestCryptage(unittest.TestCase):
    def setUp(self):
        self.instance = Cryptage()

    def test_crypt_message(self):
        self.assertEqual(self.instance.crypt("abc"), "bcd") 

if __name__ == "__main__":
    unittest.main()
