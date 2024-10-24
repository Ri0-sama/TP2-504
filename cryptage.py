import string

class Cryptage:

#Fonction de cryptage    
    def crypt(self, message, pas=1):
        caracteres = string.ascii_letters + string.digits + string.printable
        result = ""
        for char in message:
            if char in caracteres:
                index = caracteres.index(char)
               
                new_index = (index + pas) % len(caracteres)
                result += caracteres[new_index]
            else:
                result += char 
        return result


# Fonction de decryptage
    def decrypt(self, message, pas=1):
        caracteres = string.ascii_letters + string.digits + string.printable
        result = ""
        for char in message:
            if char in caracteres:
                index = caracteres.index(char)
                
                new_index = (index - pas) % len(caracteres)
                result += caracteres[new_index]
            else:
                result += char  
        return result
