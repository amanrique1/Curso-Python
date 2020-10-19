from io import open
#el archivo se puede abrir en 3 modos lectura, escritura y append(para editar un archivo ya existente)

#escribir
archivoTexto=open("archivo.txt","w") #la w es para write

frase="gran dia para estudiar python \ndomingo antes de clase"

archivoTexto.write(frase)
archivoTexto.close()


#leer
archivoTexto=open("archivo.txt","r") #la r es para read


texto=archivoTexto.read()
#si usamos readlines las lineas nos quedan en almacenadas en una lista 
archivoTexto.seek(0)  #le decimos que devuelva el puntero nuevamente al principio. El 0 lo manda al caracter 0
#si no usara el metodo anterior no habria nada en frases puesto que ya no hay nada mas para leer
frases=archivoTexto.readlines()

archivoTexto.close()

print(texto)
print(frases[0])

#editar
archivoTexto=open("archivo.txt","a") #la a es de append

archivoTexto.write("\nsiempre es un buen dia para estudiar python")

archivoTexto.close()

#lectura y escritura
archivoTexto=open("archivo.txt","r+") 

listaTexto=archivoTexto.readlines()
listaTexto.insert(1,"Esta linea ha sido incluida desde el exterior\n")
archivoTexto.seek(0)
archivoTexto.writelines(listaTexto)
archivoTexto.close