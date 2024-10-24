import unittest
from cryptage import Cryptage

class TestCryptage(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = Cryptage()

    def test_crypt_message(self):
        self.assertEqual(self.instance.crypt("abc"), "cab")  

if __name__ == "__main__":
    unittest.main()
