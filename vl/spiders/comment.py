from urllib.request import Request
import scrapy
import json

class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['vl.ru']

    start_urls = ["https://www.vl.ru/kafe-kitaj", "https://www.vl.ru/mukata", "https://www.vl.ru/mamma-mia", "https://www.vl.ru/phali-hinkali"]
    

    #/commentsgate/ajax/thread/company/yantarnaya/embedded - Get CompanyID
    #/commentsgate/ajax/comments/{CompanyID}/rendered?before=0 - Snached

    host = "https://www.vl.ru/"
    getID_A = "commentsgate/ajax/thread/company/"
    getID_B = "/embedded"
    getComment_A = "/commentsgate/ajax/comments/"
    getComment_B = "/rendered?before=0"


    # Обрабатывать ссылки полученные во время парсинга объектов
    def start_requests(self):
        for url in self.start_urls:
            scrapy.http.Response().follow(f"{self.host}{self.getID_A}{url.split('/')[-1]}{self.getID_B}",callback = self.parseID)

    # Получить ID и отправить на получение комментариев
    def parseID(self, response):
        cheiSon = json.loads(response.text)

        id = None
        if 'date' in cheiSon:
            if 'threadId' in cheiSon['data']:
                id = cheiSon['date']['threadId']

        url = f"https://www.vl.ru//commentsgate/ajax/comments/{id}/rendered?before=0"

        yield response.follow(url,callback=self.parseComment,headers = self.headers)

        
    # Художественный фильм "Спарсили"
    def parseComment(self, response):

        #yield response.json();

        #lastCommentId

        j = json.loads(response.text)
        
        q = None

        #Обход всех страниц с комментариями (Старый тестовый код)
        if 'data' in j: 
            if 'lastCommentId' in j['data']:
                q = j['data']['lastCommentId']
                yield {'lastComment':j['data']['lastCommentId']}
                yield {'content':j['data']['content']}
            else:
                q = None
        else:
            q = None
        

        


        if (q==None):
            return

        url = f'{self.a}{self.b}{q}{self.c}'

        print(f'\n\n\n\n\n\n\n\n{q}\n\n\n\n\n\n{url}\n\n')

        # Снимаем Художественный фильм "Спарсили2"
        yield response.follow(url,callback=self.parse,headers = self.headers)

        pass