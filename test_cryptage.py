# test_cryptage.py
import unittest
from cryptage import Cryptage

class TestCryptage(unittest.TestCase):
    def setUp(self):
        self.instance = Cryptage()

    

    def test_crypt_message(self):
        message = "abc"
        encrypted = self.instance.crypt(message)
        print(f"Message brut: '{message}' => Message crypté: '{encrypted}'")
        self.assertEqual(encrypted, "bcd") 

    def test_decrypt_message(self):
        encrypted_message = "bcd"
        decrypted = self.instance.decrypt(encrypted_message)
        print(f"Message crypté: '{encrypted_message}' => Message décrypté: '{decrypted}'")
        self.assertEqual(decrypted, "abc")  

if __name__ == "__main__":
    unittest.main()
