import string

class Cryptage:
    def crypt(self, message, pas=1):
        caracteres = string.ascii_letters + string.digits + string.printable
        result = ""
        for char in message:
            result += chr(ord(char) + pas)  # parametre de pas ajouté
        return result
