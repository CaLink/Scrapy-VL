from email import header
from gc import callbacks
from urllib.request import Request
from wsgiref import headers
from html2text import re
import scrapy
import json


class CheckSpider(scrapy.Spider):
    name = 'check'
    allowed_domains = ['www.vl.ru']


    #/commentsgate/ajax/thread/company/yantarnaya/embedded - Get CompanyID
    #/commentsgate/ajax/comments/{CompanyID}/rendered?before=0 - Snached


    

    #a = 'https://www.vl.ru/commentsgate/ajax/comments/1822/rendered?theme=company&appVersion=2022422161646&_dc=0.9354189651223248'
    #b = '&before='
    #c = '&pastafarian=88835d7f09f5a6895a61d29d02ee3667509e8aa8f84ed2564c72ff4122024bde&moderatorMode=1&commentAttributes%5BcommentType%5D%5B%5D=review'

    #url = 'https://www.vl.ru/commentsgate/ajax/comments/1628/rendered?theme=company&appVersion=2022422161646&_dc=0.8082369871803954&before=5189591&pastafarian=34fdc99f97fcd3a72f3ac68c3dc520aca7dd6cd0d612dfd3915bb5ca99aad2a2&moderatorMode=1&commentAttributes%5BcommentType%5D%5B%5D=review '

    url = 'https://www.vl.ru/commentsgate/ajax/thread/company/mys-balyuzek/embedded'

    headers = {
         'Cookie': 'PHPSESSID=tadetm1sujglsjm7j28uf1063f; city=4; region=103; visitor=1aeee62b8f9829178c76bd7183c5b2a64e3d72185d47ef217ae35a6acda01767; ring=5a6b3a92117e2c065144ee385c949042; log_ident=relaxbase; pastafarian=34fdc99f97fcd3a72f3ac68c3dc520aca7dd6cd0d612dfd3915bb5ca99aad2a2; _ga=GA1.2.953827.1649252252; _ga=GA1.3.953827.1649252252; _ym_d=1649252252; _ym_uid=1649252252120820961; sprRecentlyWatchedCompanyIds=22352.179467',
         'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="99"',
         'Accept': 'application/json, text/javascript, */*; q=0.01',
         'X-Requested-With': 'XMLHttpRequest',
         'Sec-Ch-Ua-Mobile': '?0',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
         'Sec-Ch-Ua-Platform': "Windows",
         'Sec-Fetch-Site': 'same-origin',
         'Sec-Fetch-Mode': 'cors',
         'Sec-Fetch-Dest': 'empty',
         'Referer': 'https://www.vl.ru/mys-balyuzek',
         'Accept-Encoding': 'gzip, deflate',
         'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    def start_requests(self):

        yield scrapy.http.Request(self.url, headers=self.headers)

    first = "13704304"



    #Проводил тестирование реквестов.
    #текущий - получение ID
    #Ниже закоментированное - тестировал пробежку по все страницам комментариев

    #ПРОБЛЕМА - после ребута машины перестал работать (haha, classic)
    #Проблема поменьше - не совсем понятно как он работает с тригеррами. Бывает что не работает без них, а бывает нормально


    def parse(self, response):
        
        
        cheiSon = json.loads(response.text)

        id = None #Need to be none
        if 'date' in cheiSon:
            if 'threadId' in cheiSon['data']:
                id = cheiSon['date']['threadId']

        url = f"https://www.vl.ru//commentsgate/ajax/comments/{id}/rendered?before=0"
        print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n{id}\n\n')
        q = Request(url,headers = self.headers)

        yield q
        
        

        # #yield response.json();

        # #lastCommentId

        # j = json.loads(response.text)
        
        # q = None


        # if 'data' in j: 
        #     if 'lastCommentId' in j['data']:
        #         q = j['data']['lastCommentId']
        #         yield {'lastComment':j['data']['lastCommentId']}
        #         yield {'content':j['data']['content']}
        #     else:
        #         q = None
        # else:
        #     q = None
        

        


        # if (q==None):
        #     return

        # url = f'{self.a}{self.b}{q}{self.c}'

        # print(f'\n\n\n\n\n\n\n\n{q}\n\n\n\n\n\n{url}\n\n')

        # yield response.follow(url,callback=self.parse,headers = self.headers)


        
