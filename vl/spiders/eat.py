from gc import callbacks
from itertools import zip_longest
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from vl.items import VlItem

class EatSpider(CrawlSpider):
    name = 'eat'
    allowed_domains = ['www.vl.ru']
    #start_urls = ['https://www.vl.ru/vladivostok/cafe','https://www.vl.ru/vladivostok/fun','https://www.vl.ru/travel']
    start_urls = ['https://www.vl.ru/vladivostok/cafe']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=["//a[contains(., 'следующая >')]"]),"parse",follow=True),
        #Rule(LinkExtractor(restrict_xpaths=["//a[contains(., 'следующая >')]"]),"parse"),
        Rule(LinkExtractor(restrict_xpaths=["//h4"]),"parse_page")
        )

    
    def parse(self, response):
        yield {"page_num":response.url}

    def parse_page(self, response):

        item = VlItem()
        
        item['Title'] = response.xpath('//h1/text()').get()
        item['URL'] = response.url
        item['Rate'] = response.xpath("//ul[@class='stars control']/@data-default").get()
        item['SubClass'] = response.xpath("//h3[@class='activity-type']/text()").get()
        item['Tags'] = []

        q = None
        if (response.xpath("//a[contains (@class,'j_showAllAttributes')]")):
            q = response.xpath("//div[@class='attributes-modal-content j_attributesModal']/div[@class='spr-attributes']")
        else:
            q = response.xpath("//div[@class='spr-attributes']")

        
        Titles = q.xpath("//div[@class='spr-attribute__title ']/span/text()").getall()
        
        params = []
        for par in q.xpath("//div[@class='spr-attribute__body']"):
            if(par.xpath("a")):
                params.append(par.xpath("a/text()").getall())
            else:
                params.append(par.xpath("span/text()").getall())

        Tags = list(zip_longest(Titles,params,fillvalue='debug'))
        
        item['Tags'] = Tags




        yield item
