import string

class Cryptage:
    def crypt(self, message):
        caracteres = string.ascii_letters + string.digits + string.printable
        result = ""
        for char in message:
            if char in caracteres:  
                result += chr(ord(char) + 1)  
            else:
                result += char  
        return result
