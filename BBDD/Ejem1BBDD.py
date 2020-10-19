#Vamos a importar la libreria sqlite que va a ser nuestro SMBD, este tambien puede ser mySql, Oracle, etc
#cordarse que sqlite no recibe consultas con where
import sqlite3

#Vamos a abrir/crear conexion. Si ya esta creada no hace nada, sino existe entonces la crea
miConexion=sqlite3.connect("PrimeraBase")

#Creamos el puntero que es el que ejecuta las consultas
puntero=miConexion.cursor()
"""
puntero.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
puntero.execute("INSERT INTO PRODUCTOS VALUES ('BALON',15,'DEPORTES')")
listaProductos=[
	("Camiseta",10,"Deportes"),
	("Jarron",90,"Ceramica"),
	("Camion",20,"Juguetes"),
	("Jean",45,"Ropa")
]

#Vamos a ejecutar una consulta para meter todo pero cada interrrogante representa una columna
puntero.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",listaProductos)

#Hacemos el commit de la transaccion
miConexion.commit()
"""
#Vamos a hacer un select sencillo, el fetchall trae lo que encontro la consulta anterior
puntero.execute("SELECT * FROM PRODUCTOS")
listaProductos=puntero.fetchall()

for prodAct in listaProductos:
	print("NOMBRE_ARTICULO: "+prodAct[0]+ " PRECIO: "+str(prodAct[1])+" SECCION: "+prodAct[2])

#Cerramos la conexion
miConexion.close()
