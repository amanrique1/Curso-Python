import math
mat=[[1,20,6],[2,22,1],[3,9,2],[4,3,25],[5,21,10],[6,29,2],[7,14,12]]
costos=[]
for nodo1 in mat:
	fila=[]
	for nodo2 in mat:
		if nodo1==nodo2:
			fila.append(0)
		else:
			distancia=math.sqrt(pow(nodo1[1]-nodo2[1],2)+pow(nodo1[2]-nodo2[2],2))
			if distancia>20:
				distancia=1000
			fila.append(distancia)
	costos.append(fila)

print(costos)