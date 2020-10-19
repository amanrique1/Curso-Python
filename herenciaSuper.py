class Persona():

	def __init__(self,nombre,edad,lugar):

		self.nombre=nombre
		self.edad=edad
		self.lugar=lugar

	def descripcion(self):

		print("Nombre: ", self.nombre, " Edad: ", self.edad , " Nacionalidad: ", self.lugar)

class Empleado(Persona):

	def __init__(self,salario,antiguedad,nombreEmp,edadEmp,lugarEmp):

		super().__init__(nombreEmp,edadEmp,lugarEmp)
		self.salario=salario

		self.antiguedad=antiguedad

	#creamos este matedo para que ademas de poner la descripcion de la persona tambien salga la de empleado 
	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario,"Antiguedad",self.antiguedad)

pedro=Empleado(5000000,15,"Pedro",55,"Bogota")
pedro.descripcion()
#Queremos saber si pedro es un empleado
print(isinstance(pedro,Empleado))

#Queremos saber si pedro es una persona
print(isinstance(pedro,Persona))


juan=Persona("Juan",22,"Venezuela")
print(isinstance(juan,Empleado))   #saber si juan es persona