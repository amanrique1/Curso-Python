import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

	# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="https://bogota.olx.com.co/apartamentos-casas-venta-cat-367"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
#html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(webpage, 'lxml')
tags = soup('li')
for tag in tags:
	#if tag.attrs == {'class': ['item ']} or tag.attrs =={'class': ['item  highlighted']} :
	#print('TAG:', tag)
	#print('URL:', tag.get('href', None))
	#print('Contents:', str(tag.contents[0].text))
	#print(str(tag.attrs).find("'class': ['masonry-item', 'highlighted']"))
	try:
		print('Contents:', tag.contents[1])
	except:
		print(" ")

	#print('Attrs:', tag.attrs)


	# Retrieve all of the anchor tags
	#tag = soup.find('span', {'class': "widget-pane-link"})
	#print(tag)
	"""
	url="https://www.properati.com.co/tools/valuator?place=bogota-d-c-colombia&address="+parte1+"+"+numero+"+%23"+complemento+"%2C+Bogot%C3%A1%2C+Colombia&operation_id=2&type_id=1&bedrooms="+cantCuartos+"&bathrooms="+cantBanios+"&stratum="+estrato+"&surface_covered="+tamanio+"&surface_uncovered=0&garage="+parqueo+"&amenities=on&point="+latitud+"%2C"+longitud+"&viewport="+latitud+"%2C"+longitud+"%2C9"
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	web_byte = urlopen(req).read()

	webpage = web_byte.decode('utf-8')
	#html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(webpage, 'lxml')
	# Retrieve all of the anchor tags
	tags = soup('li')
	for tag in tags:
		#if tag.attrs == {'class': ['item ']} or tag.attrs =={'class': ['item  highlighted']} :
		print('TAG:', tag)
		#print('URL:', tag.get('href', None))
		#print('Contents:', str(tag.contents[0].text))
		#print(str(tag.attrs).find("'class': ['masonry-item', 'highlighted']"))
		print('Contents:', tag.contents[0])
		print('Attrs:', tag.attrs)
	"""

