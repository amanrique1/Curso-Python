import pickle
#Por cada ejecucion se cargan las personas anteriores y las nuevas que agreguemos. 
#Si se agrega una misma persona en el fichero se vuelve a añadir quedn asi tantas veces como haya ejecutado
class Persona:

	def __init__(self,pNombre,pGenero,pEdad):
		self.genero=pGenero
		self.nombre=pNombre
		self.edad=pEdad
		print("Se ha creado una persona nueva con el nombre de ",self.nombre)

	def __str__(self):  #este metodo es para convertir el objeto en string, es un metodo de python
		return "Nombre:{} --- Genero:{} --- Edad:{}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
	personas=[]

	def __init__(self):
		listaPersonas=open("ficheroExterno","ab+") #ab+ es para agregar info binaria
		listaPersonas.seek(0) #desplazamos el cursor al principio
		try:
			self.personas=pickle.load(listaPersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero esta vacio")

		finally:
			listaPersonas.close()
			del(listaPersonas)

	def agregarPersonas(self,persona):
		self.personas.append(persona)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for actual in self.personas:
			print(actual)

	def guardarPersonasEnFicheroExterno(self):
		listaPersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas,listaPersonas) #aqui le pasamos la lista de personas que esta en self.personas al escritor del documento que llamamos listaPersonas
		listaPersonas.close()
		del(listaPersonas)

	def mostrarInfoFichero(self):
		print("La info del fichero es:")
		for perActual in self.personas:
			print(perActual)

miLista=ListaPersonas()
p=Persona("Andres","M",18)
miLista.agregarPersonas(p)
p=Persona("Camilo","M",30)
miLista.agregarPersonas(p)
p=Persona("Ana","F",10)
miLista.agregarPersonas(p)
miLista.mostrarInfoFichero()

