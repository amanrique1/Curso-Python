import math

def divide():
	try:
		op1=(float(input("Introduce el primer numero: ")))
		op2=(float(input("Introduce el segundo numero: ")))

		print("La division es: "+str(op1/op2))
	except ValueError:
		print("El valor introducido es erroneo")
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
	except:
		print("Ha ocurrido un error")
	finally: #Lo que esta en el finally se ejecuta siempre
		print("Calculo finalizado")

divide()

def evaluaEdad(edad):
	if edad<0:
		raise TypeError("Edad negativa")

	if edad<18:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	else:
		return "cuidate"

def calcularRaiz(num1):
	if num1<0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:
		print(calcularRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)