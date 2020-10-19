from io import open
import random
#el archivo se puede abrir en 3 modos lectura, escritura y append(para editar un archivo ya existente)


i=0
frase=""
archivoTexto=open("1000000numbers.txt","w") #la w es para write
for i in range(1000000):
	frase=""
	j=random.random()*random.random()
	frase=frase+str(j)+"\n"
	archivoTexto.write(frase)
	i+=1
archivoTexto.close()