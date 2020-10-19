import matplotlib.pyplot as plt
import numpy as np

def darArcos(costos):
	adyacentes=[]
	for i in range(len(costos)):
		if(costos[i]<=14):
			adyacentes.append((i,costos[i]))
	return adyacentes



plt.style.use('ggplot')
inicial=input("Digite el nodo inicial: ")
final=input("Digite el nodo final: ")

puntos=np.random.rand(2,100)
puntos=[puntos[0]*100,puntos[1]*100]
costo=np.random.rand(100,100)
for i in range(100):
    for j in range(100):
        if i!=j:
            costo[i][j]=( (puntos[0][j]-puntos[0][i])**2+(puntos[1][j]-puntos[1][i])**2)**(1/2)
            if costo[i][j]>14:
                costo[i][j]=np.inf
        else:
            costo[i][j]=0
marcados={}
porRevisar=[inicial]
dijkstra=np.zeros((100,2))
for i in range(100):
    dijkstra[i][1]=np.inf
    dijkstra[i][0]=None

dijkstra[int(inicial)][0]=inicial
dijkstra[int(inicial)][1]=0

while len(porRevisar)>0:
	nodo=porRevisar[0]
	porRevisar.remove(nodo)
	nodo=int(nodo)
	marcados[nodo]=1

	arcos=darArcos(costo[nodo])
	for arco in arcos:
		if(arco[1]+dijkstra[nodo][1]<dijkstra[int(arco[0])][1]):
			dijkstra[int(arco[0])][1]=arco[1]+dijkstra[nodo][1]
			dijkstra[arco[0]][0]=nodo
		if arco[0] not in marcados.keys():
			porRevisar.append(arco[0])
print(dijkstra[int(final)])
rutax=[puntos[0][int(final)]]
rutay=[puntos[1][int(final)]]
if dijkstra[int(final)][0] is not None:
    origen=int(final)
    path=[dijkstra[int(final)][0]]
    while origen!=int(inicial):
        origen=int(origen)
        rutax.append(puntos[0][int(dijkstra[origen][0])])
        rutay.append(puntos[1][int(dijkstra[origen][0])])
        path.insert(0,dijkstra[origen][0])
        origen=dijkstra[origen][0]
    print(path)
else:
    print("No hay camino")

plt.figure(1)
plt.plot(puntos[0], puntos[1], 'ko')
plt.plot(rutax, rutay, 'ro-')
plt.axis([0, 100, 0, 100])
plt.show()