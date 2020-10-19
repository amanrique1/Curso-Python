#join(cadena) para concatenar de una manera mas eficiente (espacio en memoria)
#upper() convertir en mayusculas todas las letras
#lower() convertir en minusculas todas las letras
#capitalize() poner SOLO la primera letra en mayuscula
#count() cuenta cuantas veces aparece una cadena o un caracter dentro de una frase
#find() posicion en la que aparece un caracter o una palabra dentro de un texto
#index() posicion en la que aparece un caracter o una palabra dentro de un texto, lanza excepcion sino lo encuentra
#isdigit() true/false si el string es un numero
#isalum() true/false si el string es alfa-numerico
#isalpha() true/false si son solo letras
#split() separa palabras por espacios
#strip() borra los espacios sobrantes al principio y al final
#replace() cambia una palabra o una letra por otra
#rfind() posicion en la que aparece un caracter o una palabra empezando desde el final
#len(cadena) cantidad de caracteres de la cadena
#http://pyspanishdoc.sourceforge.net/lib/string-methods.html

nombre=input("Introduce tu nombre de usuario: ")
edad=input("Introduce tu edad: ")
print("El nombre es", nombre)
print("El nombre es", nombre.upper())
print("El nombre es", nombre.lower())
print("El nombre es", nombre.capitalize())
print(edad.isdigit())


correo=input("Introduce tu email ")
try: 
	posicion=correo.index("@")
	if(correo.count("@")>1):
		print("email incorrecto")

	elif(posicion==0):
		print("email incorrecto")

	elif(posicion==(len(correo)-1)):
		print("email incorrecto")

	else:
		print("email correcto")

except:
	print("email incorrecto")
