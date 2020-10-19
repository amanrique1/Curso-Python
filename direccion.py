"""
from geopy.geocoders import Nominatim

geolocator=Nominatim()
ubicacion=geolocator.reverse("4.724,-74.065")
print(ubicacion.raw)

"""

from geopy.geocoders import GoogleV3
import requests
from bs4 import BeautifulSoup


def main_spider(url):
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'html.parser')
	precio = soup.find('div', {'class': "results-found"}).find('h3').string
	return precio



valorSolicitado='$599.000.000'
cantCuartos='3'
cantBanios='3'
estrato='5'
tamanio='91'
parqueo='on'
latitud="4.70380163192749"
longitud="-74.0520248413086"
punto=latitud+","+longitud
geolocator=GoogleV3(api_key="")
direccion=geolocator.reverse(punto)
direccion=direccion[0]
y = direccion.split(",")
direccion=y[0]
print("Valor solicitado: "+valorSolicitado)
print("Cuartos: "+cantCuartos)
print("Baños: "+cantBanios)
print("Estrato: "+estrato)
print("Area: "+tamanio)
print("Parqueo: "+parqueo)
print("Ubicacion: [" +punto+"]")
print("Direccion: "+direccion)
direccion=direccion.replace(' ','+')
url="https://www.properati.com.co/tools/valuator?place=bogota-d-c-colombia&address="+direccion+""\
    "%2C+Bogot%C3%A1%2C+Colombia&operation_id=2&type_id=1&bedrooms="+cantCuartos+"&bathrooms="+cantBanios+""\
    "&stratum="+estrato+"&surface_covered="+tamanio+"&surface_uncovered=0&garage="+parqueo+"&amenities=on&point="\
    ""+latitud+"%2C"+longitud+"&viewport="+latitud+"%2C"+longitud+"%2C9"
print("URL: "+url)
precio=main_spider(url)
print(precio)




"""
import math
def distanciaEnMetros( pickupLatitud,  pickupLongitud, pLat,  pLon,  conDistRef): 

	try:

		r=6371*1000
		latDist=toRad(pickupLatitud-pLat)
		lonDist=toRad(pickupLongitud-pLon)
		a = math.sin(latDist/2)*math.sin(latDist/2)+math.cos(toRad(pLat))*math.cos(toRad(pickupLatitud))*math.sin(lonDist/2)*math.sin(lonDist/2)
		c=2*math.atan2(sqrt(a), math.sqrt(1-a))
		if conDistRef:
			if distanciaReferencia>=(r*c):
				return (r*c)
			else:
				math.inf
		return (r*c);

	except:
		print("Errorrr")
		return math.inf



def toRad( grados):
	return (grados/180)*math.pi

print(math.sin(toRad(90)))
"""