"""
Encapsulamiento: nivel de acceso a los datos y funciones
atrib: publico
_atrib: protected
__atrib: privado
Para acceder a un tributo dentro de la clase se usa la misma convencion (nada _ o __)
para acceder fuera de la clase(ya instanciado) se usa obj_Clase__nombreFuncionOATrib (para los privados, el resto se mantiene con la convencion nada o _)
"""
class Carro():

	#Vamos a crear el constructor
	def __init__(self):
		self.largoChasis=250 #Asi el atributo se declararia publico
		self.__anchoChasis=120 #Esto seria el equivalente a decir private ruedas (encapsulamiento) es decir, no permite que se modifique el valor afuera de la clase
		self._ruedas=4   #Esto es el equivalente a decir protected
		self.__andando=False

	def setArranque(self,estado):
		self.__andando=estado
		if(self.__andando and self.__chequeoInterno()):
			print("Todo esta correcto")
		elif(self.__andando):
			print("Hay algun problema")

	def darEstado(self):
		print("El carro tiene ",self._ruedas," ruedas. Un ancho de ",self.__anchoChasis)

	#Creo un metodo privado
	def __chequeoInterno(self):
		print("Realizando chequeo interno")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas" ):
			return True
		else:
			return False

carrito=Carro()

print("El largo del carro es: ",carrito.largoChasis)
print("El ancho del carro es: ",carrito._Carro__anchoChasis)
print("Vamos a arrancar")
carrito.setArranque(True)
carrito.darEstado()