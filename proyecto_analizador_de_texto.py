texto = input("Escriba un texto, poema, oracion, letra de musica o literalmente lo que sea: ")

#Contar cuantas veces se repiten las letras "a", "b" y "c".

letras = []

texto.lower()

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

contador = f"La letra '{letras[0]}' se repite {contador1} veces, la '{letras[1]}' {contador2} veces y la '{letras[2]}' {contador3} veces"
print(contador)
print("")

#Contar cuantas palabras hay en el texto.

palabras = texto.split()
print(f"En el texto hay {len(palabras)} palabras")
print("")

#Identificar primera y ultima letra

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es {primera_letra} y la ultima es {ultima_letra}")
print("")

#palabras en orden inverso

palabra = texto.split()
palabra_invertida = reversed(palabra)
texto_invertido = " ".join(palabra_invertida)
print(f"Texto invertido: {texto_invertido}")
print("")

#Identificar si aparece la palabra "python"

encontrar_python = "Python" in texto
if encontrar_python == True:
    print("La palabra 'python' si aparece en el texto")
else:
    print("La palabra 'python' no aparece en el texto")






