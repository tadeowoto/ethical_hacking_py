import hashlib

def calc_hash(string):
    """
    :param string: string to hash
    :return: hashed string
    """
    #sha256 es un algoritmo de hash hexadecimal de 64 caracteres
    sha256 = hashlib.sha256()
    #el .update calcula la huella
    sha256.update(string.encode('utf-8')) # convierte el string a bytes y lo envia al algoritmo de hash
    
    return sha256.hexdigest() # retorna la huella en formato hexadecimal

print("----------------")
print(calc_hash('hola'))
print("----------------")