texto = input("Escriba un texto, poema, oracion, letra de musica o literalmente lo que sea: ")

#Contar cuantas veces se repiten las letras

letras = []

texto.lower()
print("")
print("Elije letras a eleccion para contarlas: ")
print("")
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())
print("")
print("CANTIDAD DE LETRAS")
contador1 = texto.count(letras[0])
contador2 = texto.count(letras[1])
contador3 = texto.count(letras[2])

print(f"La letra '{letras[0]}' está repetida '{contador1}' veces")
print(f"La letra '{letras[1]}' está repetida '{contador2}' veces")
print(f"La letra '{letras[2]}' está repetida '{contador3}' veces")

print("")

#Contar cuantas palabras hay en el texto.

print("CANTIDAD PALABRAS")
palabras = texto.split()
print(f"Fueron encontradas {len(palabras)} palabras en el texto")
print("")

#Identificar primera y ultima letra

print("LETRA DE INICIO Y DE FIN")
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es '{primera_letra}' y la ultima es '{ultima_letra}'")
print("")

#palabras en orden inverso

print("TEXTO INVERTIDO")
palabra = texto.split()
palabra_invertida = reversed(palabra)
texto_invertido = " ".join(palabra_invertida)
print(f"Texto invertido: {texto_invertido}")
print("")

#Identificar si aparece la palabra "python"

print("BUSCANDO LA PALABRA 'PYTHON'")
encontrar_python = "Python" in texto
if encontrar_python == True:
    print("La palabra 'python' si aparece en el texto")
else:
    print("La palabra 'python' no aparece en el texto")