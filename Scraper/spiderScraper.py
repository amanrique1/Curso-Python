from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
import csv

class Pregunta(Item):
	posicion=Field()
	pregunta=Field()

class StackOverflowSpider(Spider):
	name="SpiderStack"
	start_urls=["https://stackoverflow.com/"]
	def parse(self,response):
		sel=Selector(response)
		#busque entre todo los divs que tiene la pagina coja el que se llame question y despues coja todos los divs que tiene este
		preguntas=sel.xpath('//div[@id="question-mini-list"]/div') 

		#Iterar sobre todas las preguntas
		for i,actual in enumerate(preguntas):
			item=ItemLoader(Pregunta(),actual)
			#buscamos el h3 donde esta la pregunta que buscamos
			item.add_xpath('pregunta','.//h3/a/text()')
			item.add_value('posicion',i)
			yield item.load_item()
