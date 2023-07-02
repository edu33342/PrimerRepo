import random
import string
 
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña
 
longitud = 10 # longitud de la contraseña (puede adaptarse para diferentes tamaños)
nueva_contraseña = generar_contrasena(longitud) # llamamos al método de generación de contraseñas
 
print("Tu nueva contraseña es: ", nueva_contraseña)
