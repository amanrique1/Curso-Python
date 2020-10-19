class Carro():

	def desplazamiento(self):
		print ("Usando 4 ruedas")

class Moto():

	def desplazamiento(self):
		print ("Usando 2 ruedas")

class Camion():

	def desplazamiento(self):
		print ("Usando 6 ruedas")

vehiculo=Moto()
vehiculo.desplazamiento()

vehiculo2=Carro()
vehiculo2.desplazamiento()

vehiculo3=Camion()
vehiculo3.desplazamiento()

def desplazamientoVehiculo(pVehiculo):
	pVehiculo.desplazamiento()

desplazamientoVehiculo(vehiculo)
desplazamientoVehiculo(vehiculo2)
desplazamientoVehiculo(vehiculo3)