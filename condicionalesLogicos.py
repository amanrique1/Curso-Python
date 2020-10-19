print("Programa de becas")
distUni=int(input("Digite su distancia a la universidad en km: "))
cantHermanos=int(input("Digite la cantidad de hermanos: "))
salario=int(input("Digite el salario familiar: "))

if (distUni>40 and cantHermanos>2) or salario<=20000:
	print("Tiene derecho a beca")
	uni=input("Seleccione la Universidad a la cual aplica: Andes - Nacional - Javeriana - Sabana - Otra\n")
	#Para evitar los errores con minusculas o mayusculas pasamos las opciones todas en minusculas y convertimos el texto de entrada todo a minuscula con la funcion lower. 
	#lomer es para minuscula
	#upper es para mayuscula
	universidad=uni.lower()
	if universidad in ("andes","nacional","javeriana","sabana"):
		print("Su beca ahora se encuentra en proceso")
	else:
		print("Por favor comuniquese con el ICETEX")

else:
	print("No tiene derecho a beca")