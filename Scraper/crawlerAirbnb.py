from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
import csv

class AirbnbItem(Item):
	tipo=Field()
	capacidad=Field()

class AirbnbCrawler(CrawlSpider):
	name="SpiderAirbnb"
	start_urls=["https://www.airbnb.com.co/s/Londres--Reino-Unido"]
	allowed_domains=['airbnb.com']

	rules={
	Rule(LinkExtractor(allow=r'items_offset=')),
	Rule(LinkExtractor(allow=r'/rooms'),callback='parse_items'),
	}

	def parse_items(self,response):
		item=ItemLoader(AirbnbItem(),response)
		item.add_xpath('tipo',"/html/body/div[3]/div/main/div/section/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div/div[1]/div[2]/div[1]/text()")
		item.add_xpath('capacidad','/html/body/div[3]/div/main/div/section/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div/div[1]/div[2]/div[2]/div[3]/div/text()',MapCompose(lambda i:i[0]))
		yield item.load_item()