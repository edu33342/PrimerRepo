texto = input("Escriba un texto, poema, oracion, letra de musica o literalmente lo que sea: ")

#Contar cuantas veces se repiten las letras "a", "b" y "c".

texto.lower()
contador_a = texto.count("a")
contador_b = texto.count("b")
contador_c = texto.count("c")

contador = f"La letra 'a' se repite {contador_a} veces, la 'b' {contador_b} veces y la 'c' {contador_c} veces"
print(contador)

#Contar cuantas palabras hay en el texto.

palabras = texto.split()
print(f"En el texto hay {len(palabras)} palabras")

#Identificar primera y ultima letra

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es {primera_letra} y la ultima es {ultima_letra}")

#palabras en orden inverso

palabra = texto.split()
palabra_invertida = reversed(palabra)
texto_invertido = " ".join(palabra_invertida)
print(f"Texto invertido: {texto_invertido}")

#Identificar si aparece la palabra "python"

encontrar_python = "Python" in texto
if encontrar_python == True:
    print("La palabra 'python' si aparece en el texto")
else:
    print("La palabra 'python' no aparece en el texto")






