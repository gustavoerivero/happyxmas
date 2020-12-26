# Se importan las librerías necesarias para el funcionamiento del archivo.
from playsound import playsound

# Se declaran las variables.
num     = 10
name    = input("\nIngrese su nombre: ")

# Se construye el árbol navideño.
print("")

for i in range(num):
    print(" " * (num - i - 1) + "*" * (2 * i + 1))

for n in range(int (num/2)):
    print(" " * int(num - num/4) + "|" * int(num/2))

print("")

# Se indica el mensaje.
print("FELIZ NAVIDAD PARA TODOS DE PARTE DE " + name.upper())

# Se reproduce la canción.
playsound('Feliz Navidad 8-bit.mp3')
