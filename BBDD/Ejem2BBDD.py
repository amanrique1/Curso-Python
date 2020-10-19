import sqlite3


miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

#Si uno quiere escribir en varias lineas puede usar comilla 3 para que no marque error
"""
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	 ID INTEGER PRIMARY KEY AUTOINCREMENT,
	 NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	 PRECIO INTEGER,
	 SECCION VARCHAR(20))''')

listaProductos=[
	("Camiseta",10,"Deportes"),
	("Jarron",90,"Ceramica"),
	("Camion",20,"Juguetes"),
	("Jean",45,"Ropa")
]

#Vamos a ejecutar una consulta para meter todo pero cada interrrogante representa una columna
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",listaProductos)

#Hacemos el commit de la transaccion
miConexion.commit()
"""
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Ceramica'")
productos=miCursor.fetchall()
print (productos)

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Jean'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=3")


miConexion.commit()
miConexion.close()
