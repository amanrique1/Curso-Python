class Vehiculos():

	def __init__(self,marca,modelo):

		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):

		self.enMarcha=True

	def acelerar (self):
		self.acelera=True

	def frenar (self):
		self.frena=True

	def darEstado(self):
		print("Marca: ",self.marca, "\nModelo: ", self.modelo)

class VElectrico(Vehiculos):
	def __init__(self,marca,modelo):
		self.autonomia=100
		super().__init__(marca,modelo)

	def cargarEnergia(self):
		self.cargado=True



class Moto(Vehiculos):
	hCaballito=""

	def caballito(self):
		self.hCaballito="Voy haciendo caballito"

		#Estamos sobre escribiendo el metodo de darEstado
	def darEstado(self):
		print("Marca: ",self.marca, "\nModelo: ", self.modelo,"\n",self.hCaballito)


class Furgoneta(Vehiculos):
	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"
#Vamos a hacer una clase con herencia multiple
#Si hay metodos con el mismo nombre en ambas clases padre como es el caso del constructor (metodo init) tiene prevalencia el que escribamos primero en este caso velectrico
class BiciElectrica(VElectrico,Vehiculos):
	pass


miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.darEstado()

miFurgo=Furgoneta("Renault","Kangoo")
miFurgo.arrancar()
miFurgo.darEstado()
print(miFurgo.carga(True))

miBici=BiciElectrica("Orbea","hj")
print(miBici.autonomia)