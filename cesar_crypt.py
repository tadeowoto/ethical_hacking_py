# CRIPTOGRAFÍA CLÁSICA EN GOOGLE COLAB
# Materia: Seguridad Informática
# Tema: Cifrado César y Atbash
# Ing. Astri Edith Andrada Tivani

# --- Introducción teórica ---
# En esta práctica vamos a explorar dos métodos clásicos de cifrado: el Cifrado
# César y el Cifrado Atbash.
# Ambos pertenecen a la criptografía de sustitución, donde cada letra del
#mensaje original se reemplaza por otra.

# Cifrado César:
# Es un tipo de cifrado por desplazamiento. Cada letra del mensaje se reemplaza
# por otra
# que esté un número fijo de posiciones más adelante en el alfabeto.
# Por ejemplo, con desplazamiento 3:
# "ATAQUE" -> "DWDTXH"
#
# Cifrado Atbash:
# Es un método de sustitución específico donde la primera letra se reemplaza
#por la última, la segunda por la penúltima, etc.
# "ATAQUE" -> "ZGZJFP"

# --- Implementación del Cifrado César ---
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            codificada = chr((ord(letra) - base + desplazamiento) % 26 + base)
            resultado += codificada
        else:
            resultado += letra
    return resultado

def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)

# --- Implementación del Cifrado Atbash ---
def cifrado_atbash(texto):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            invertida = chr(base + 25 - (ord(letra) - base))
            resultado += invertida
        else:
            resultado += letra
    return resultado

# --- Ejercicios prácticos ---
texto_original = "ATAQUE AL AMANECER"
desplazamiento = 3

print("Texto original:", texto_original)

print("\n--- CIFRADO CÉSAR ---")
cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto cifrado:", cifrado)
print("Texto descifrado:", descifrado_cesar(cifrado, desplazamiento))

print("\n--- CIFRADO ATBASH ---")
cifrado2 = cifrado_atbash(texto_original)
print("Texto cifrado:", cifrado2)

# --- Desafíos extra ---
# 1. Modifica el desplazamiento del César y probá diferentes valores.
# 2. Proba con mensajes en minúscula, con números o símbolos.
# 3. Escribí una función que detecte automáticamente si un texto está cifrado
# con Atbash y lo descifre.
# 4. Crea tu propio método de cifrado de sustitución.