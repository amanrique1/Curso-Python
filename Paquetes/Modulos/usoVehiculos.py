from moduloVehiculos import *


miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.darEstado()

miFurgo=Furgoneta("Renault","Kangoo")
miFurgo.arrancar()
miFurgo.darEstado()
print(miFurgo.carga(True))

miBici=BiciElectrica("Orbea","hj")  