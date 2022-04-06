# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VlItem(scrapy.Item):

    Title = scrapy.Field()
    URL =  scrapy.Field()
    Rate =  scrapy.Field()
    SubClass =  scrapy.Field()
    Tags = scrapy.Field()




    
