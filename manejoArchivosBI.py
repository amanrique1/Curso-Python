#importar pickle
#dump() crear archivo binario externo a partir de datos
#load() carga del archivo binario
import pickle
from herencia import *

#CREACION
listaNombres=["Pedro","Ana","Maria","Isabel"]
archBinario=open("listaNombres","wb") #wb es para escritura binaria

pickle.dump(listaNombres,archBinario)
archBinario.close()
del(archBinario)

#LECTURA

archBinario=open("listaNombres","rb") #wb es para lectura binaria
lista=pickle.load(archBinario)
print(lista)
archBinario.close()
del(archBinario)

#Creacion con objetos
carro1=Vehiculos("Mazda","MX5")
carro2=Vehiculos("Seat","Leon")
carro3=Vehiculos("Renault","Clio")
carros=[carro1,carro2,carro3]

archBinario=open("listaCarros","wb")
pickle.dump(carros,archBinario)
archBinario.close()
del(archBinario)

#Lectura de objetos

archBinario=open("listaCarros","rb") #wb es para lectura binaria
listaCarros=pickle.load(archBinario)
archBinario.close()
del(archBinario)
for i in listaCarros:
	print(i.darEstado())