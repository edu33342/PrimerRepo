from random import *
##Juego Adivina el numero

numero_aleatorio = randint(1,100)
lista = list(range(1,9))
intentos = 0
nombre = input("¿Cuál es tu nombre?: ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes solo ocho intentos para adivinar cuál crees\nque es el número")

for n in lista:
    intentos = input(f"Intento N°{n}: ")
    intentos = int(intentos)
    if intentos == numero_aleatorio:
        print(f"¡{nombre} Haz ganado en {n} intentos!")
        break
    elif intentos < 1 or intentos > 100:
        print("Haz elegido un número que no está permitido")
    elif intentos < numero_aleatorio:
        print("Respuesta incorrecta. Elegiste un número menor al número secreto")
    elif intentos > numero_aleatorio:
        print("Respuesta incorrecta. Elegiste un número mayor al número secreto")
print("")
if intentos != numero_aleatorio:
    print("Se te han agotado los intentos. Haz prdido")