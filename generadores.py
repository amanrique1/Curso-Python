#Los generadores develven solo un elemento de un iterable lo cual hace que
# no se tenga que reservar un espacio en la memoria y podamos optimizar recursos

def generarParesLista(limite):
	num=1
	misNumeros=[]
	while num<limite:
		misNumeros.append(num*2)
		num+=1
	return misNumeros

print(generarParesLista(10))
def generarParesGenerador(limite):
	num=1
	while num<limite:
		yield num*2
		num+=1

numPares=generarParesGenerador(10)

print(next(numPares))     #Imprime el siguiente elemento que en este caso seria el primero
for i in numPares:        #Impreme el resto de elementos es decir, todos menos el primero que lo imprimio arriba
	print(i)


def darCiudades(*ciudades):   #El * significa que recibe un numero indeterminado de elementos en forma de tuplas
	for elemento in ciudades:
		# Se recorre cada letra de la ciudad
		for subElemento in elemento:
			yield subElemento

def darCiudades2(*ciudades):   #Forma alternativa del metodo anterior
	for elemento in ciudades:
		# Se recorre cada letra de la ciudad sin usar un for
		yield from elemento

ciudadesR=darCiudades("Madrid","Barcelona","Bilbao","Valencia","Sevilla")
ciudadesR2=darCiudades2("Madrid","Barcelona","Bilbao","Valencia","Sevilla")
#Next es como un pop saca el 1 elemento
print(next(ciudadesR))
print(next(ciudadesR2))

ciudadesRStr =""
for letra in ciudadesR:
	ciudadesRStr = ciudadesRStr + letra
print(ciudadesRStr)

ciudadesR2Str =""
for letra in ciudadesR2:
	ciudadesR2Str = ciudadesR2Str + letra
print(ciudadesR2Str)