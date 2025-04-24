from email import message
from cryptography.fernet import Fernet

def fernet_encrypt(message, clave):
    #Creamos un objeto Fernet
    fernet = Fernet(clave)
    #el encode convierte el string a bytes
    mensaje_encriptado = fernet.encrypt(message.encode())
    return mensaje_encriptado 

def fernet_decrypt(message, clave):
    #Creamos un objeto Fernet
    fernet = Fernet(clave)
    #el decode convierte los bytes a string
    mensaje_desencriptado = fernet.decrypt(message).decode()
    return mensaje_desencriptado

mensaje = "Hola mundo"

print("Mensaje original: ", mensaje)
print('-----------------------------------------')
clave = Fernet.generate_key()
print("Clave: ", clave)
print('-----------------------------------------')
mensaje_encriptado = fernet_encrypt(mensaje, clave)
print("Mensaje encriptado: ", mensaje_encriptado)
print('-----------------------------------------')
mensaje_desencriptado = fernet_decrypt(mensaje_encriptado, clave)
print("Mensaje desencriptado: ", mensaje_desencriptado)
print('-----------------------------------------')

