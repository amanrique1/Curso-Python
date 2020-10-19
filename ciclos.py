for i in ["pedro", "pablo", "camilo", "daniel"]:
	print(i)

contador=0
email=input("Digite su correo electronico\n")
for i in email:
	print(i, end=" ")
	if(i=="@"):
		contador+=1
	elif(i=="."):
		contador+=1

if contador>=2:
	print ("\nEl email es correcto")
else:
	print ("\nEl email es incorrecto")

for i in range (5):
	print(f"valor de la variable {i}") #Concatenamos un texto con la variable de tipo range
for i in range (5,10): #Inicio-Fin
	print(f"valor de la variable {i}")
for i in range (10,50,5): #Inicio-Fin-Cada cuanto
	print(f"valor de la variable {i}")



i=0
while i<10:
	print("Ejecucion "+str(i+1))
	i+=1

edad=int(input("Intruzca su edad\n"))
intentos=1
while edad<=0 or edad>100:
	print("La edad no es correcta")
	edad=int(input("Intruzca su edad\n"))
	intentos+=1
	if intentos==3:
		break; #este si va con ;

if intentos==3:
	print("No joda tanto, no esta bien :v")
else:
	print("La edad es correcta")

cantidad=0
for letra in "Pildoras informaticas":
	if letra==" ":
		continue #El continue lo que hace es que se salte lo que viene despues y empieza la siguiente iteración
	cantidad+=1
	print(letra)
print(cantidad) #Son 21 caracteres con el espacio pero como hicimos el continue no aumenta el contador