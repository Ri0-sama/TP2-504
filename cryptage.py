class Cryptage:
    def crypt(self, message):
        result = ""
        for char in message:
            result += chr(ord(char) + 1)  # Remplace chaque caractère par le suivant dans ASCII
        return result
