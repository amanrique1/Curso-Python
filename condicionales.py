print("Mayo/Menor")
edad=input("Por favor digite la edad: ")
edad=int(edad) #Si quisiera volver a pasarlo a string tendria que usar la funcion str()
def mayoria(pEdad):
	habilitado=-1

	if pEdad>=100:
		habilitado=False
	elif pEdad>=18:
		habilitado=True
	else:
		habilitado=False
	return habilitado
def mayoria2(pEdad):
	habilitado=-1

	if 18<=pEdad<100:
		habilitado=True
	else:
		habilitado=False
	return habilitado
print(mayoria(edad))
print(mayoria2(edad))
